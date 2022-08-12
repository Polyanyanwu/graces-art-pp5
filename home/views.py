""" Home page views """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator

from utility.models import SystemPreference
from .forms import ContactUsForm, ReviewForm
from .models import Review, FAQ


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


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
