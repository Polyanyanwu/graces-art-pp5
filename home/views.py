""" Home page views """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from utility.models import SystemPreference, HomeMessage
from profiles.user_belong import check_in_group
from .forms import ContactUsForm, ReviewForm, FAQForm
from .models import Review, FAQ


def index(request):
    """ A view to return the index page """
    home_msg = ""
    try:
        # fetch the landing page message from the db
        home_msg = HomeMessage.objects.get(code='H')
    except ObjectDoesNotExist as exc:
        messages.info(request, "Welcome to Graces Art Print")
        print(exc)

    return render(request, 'home/index.html', {'msg': home_msg})


@login_required
def coupons(request):
    """ A view to return the coupon toast
            ('CF', 'Customer welcome Coupon Code'),
            ('CR', 'Customer Threshold Coupon Code'),
            ('C1', 'Welcome coupon percentage discount'),
            ('T1', 'Threshold Amount'),
            ('C2', 'Threshold discount percentage')
    """
    welcome_code = get_object_or_404(SystemPreference, code='CF').data
    welcome_code_discount = get_object_or_404(SystemPreference, code='C1').data
    threshold_code = get_object_or_404(SystemPreference, code='CR').data
    threshold_amt = get_object_or_404(SystemPreference, code='T1').data
    threshold_discount = get_object_or_404(SystemPreference, code='C2').data

    return render(request, 'home/coupons.html',
                  {
                    'welcome_code': welcome_code,
                    'welcome_code_discount': welcome_code_discount,
                    'threshold_code': threshold_code,
                    'threshold_amt': threshold_amt,
                    'threshold_discount': threshold_discount,
                  })


def contact_us(request):
    """ View to receive contact us message """

    # form = ContactUsForm()
    if request.user.is_authenticated:
        email = get_object_or_404(User, username=request.user).email
    else:
        email = ""

    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            form_message = form.save(commit=False)
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user)
                form_message.user = user
            form_message.save()
            messages.info(request, 'Thank you for your message')
            return redirect('home')
        else:
            messages.info(request, 'Please check your\
                submission and try again')
            email = request.POST.get('email')
    else:
        data = {'message_body': "", 'sender': email, 'subject': 'information'}
        form = ContactUsForm(initial=data)
    return render(
        request,
        "home/contact_us.html",
        {
                "form": form,
                "email": email
            }
        )


class WriteReviewView(View):
    """ Accept and display review records,
        requires login for post messages"""

    def get(self, request, *args, **kwargs):
        """ Display reviews to users """
        reviews = Review.objects.all().order_by('-date')
        form = ReviewForm()
        paginator = Paginator(reviews, 3)  # Show 10 per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'home/write_review.html',
                      {'reviews': page_obj,
                       'form': form, })

    def post(self, request, *args, **kwargs):
        """ save review messages
            Requires login which was done in the URL
        """
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            messages.info(request, 'Thank you for your review')
            return redirect('home')
        else:
            messages.info(request, 'Please check your\
                submission and try again')
            form = ReviewForm(request.POST)
            reviews = Review.objects.all().order_by('-date')
            paginator = Paginator(reviews, 3)  # Show 10 per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        return render(request, 'home/write_review.html',
                      {'reviews': page_obj,
                       'form': form, })


def view_reviews(request):
    """ Display reviews to users """
    reviews = Review.objects.all().order_by('-date')

    paginator = Paginator(reviews, 3)  # Show 10 per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/review.html',
                  {'reviews': page_obj, })


def view_faq(request):
    """ Display frequently asked questions to users """
    print("at request")
    faqs = FAQ.objects.all()

    return render(request, 'home/faq.html',
                  {'faqs': faqs})


@login_required
def maintain_faq(request):
    """ Maintain FAQ """
    # check that user is administrator
    rights = check_in_group(request.user, ("administrator",))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    faqs = FAQ.objects.all()
    use_instance = True
    if faqs.count() == 0:
        use_instance = False
        form = FAQForm()
    if request.method == 'POST':
        if 'select_rec' in request.POST:
            id_sent = int(request.POST.get('name_selected'))
            art_genre = get_object_or_404(FAQ, pk=id_sent)
            request.session['current_rec'] = id_sent
            form = FAQForm(instance=art_genre)
        elif 'create_new_record' in request.POST:
            form = FAQForm()
            request.session['current_rec'] = ""
        elif 'cancel_ops' in request.POST:
            if use_instance:
                form = FAQForm(instance=faqs[0])
                request.session['current_rec'] = faqs[0].id
            HttpResponseRedirect('home/maintain_faq.html')
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            name_sent = request.POST.get('confirm-id')
            faq = get_object_or_404(FAQ, id=name_sent)
            name = faq.question
            faq.delete()
            messages.success(request,
                             ('FAQ ' + name +
                              ' was successfully deleted!'))
            if faqs.count() > 0:
                form = FAQForm(instance=faqs[0])
                request.session['current_rec'] = faqs[0].id
        elif 'save_record' in request.POST:
            if request.session.get('current_rec'):
                # editing a record which id was put in session
                faq_id = int(request.session.get('current_rec'))
                faq = FAQ.objects.get(pk=faq_id)
                form = FAQForm(request.POST, instance=faq)
            else:
                form = FAQForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 ('Your FAQ was successfully saved!'))
            else:
                messages.error(request, ('Please correct the error below.'))
    else:
        if faqs.count() > 0:
            form = FAQForm(instance=faqs[0])
    paginator = Paginator(faqs, 10)  # Show 10 bookings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/maintain_faq.html', {
        'form': form,
        'faqs': page_obj,
    })
