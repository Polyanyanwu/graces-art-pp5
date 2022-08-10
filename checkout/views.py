""" Module to process checkout and payment """

from decimal import Decimal
import json
import stripe
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from bag.contexts import bag_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from profiles.user_belong import check_in_group
from utility.models import SystemPreference
from artworks.models import Artwork, ArtFrame
from .models import OrderLineItem, Order, OrderStatus, Notification
from .forms import OrderForm, ReturnOrderForm
from .query_utils import query_order


def checkout(request):
    bag = request.session.get('bag', {})
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('get_artworks'))

    bag_content = bag_contents(request)
    current_grand_total = bag_content['grand_total']

    template = 'checkout/checkout.html'
    discount_code = None
    discount = 0
    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postal_code': request.POST['postal_code'],
            'town_city': request.POST['town_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county_region': request.POST['county_region'],
            'discount_code': request.POST['discount_code'],
        }
        form = OrderForm(form_data)

        if 'apply-discount-btn' in request.POST:
            discount_code = request.POST.get('discount_code')
            if not discount_code or len(discount_code.strip()) == 0:
                messages.warning(request, "You didn't enter \
                    discount code before clicking Apply")
                return redirect('checkout')
            discount = _get_discount(request, discount_code,
                                     bag_content['total'])
            if discount == -9:
                # already used startup discount code
                messages.warning(request, "This welcome discount \
                    code has been used by you already!")
                return redirect('checkout')
            elif discount == -1:
                # less than discount threshold
                messages.warning(request, "Your total shopping does not \
                    qualify for this discount, buy more things first!")
                return redirect('checkout')
            elif discount == -2:
                # not signed in user
                messages.warning(request, "To apply discount vouchers \
                    please login first!")
                return redirect('checkout')
            current_grand_total -= discount
            bag_content['grand_total'] = current_grand_total

        else:  # submit from strip payment
            if form.is_valid():
                order = form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.stripe_pid = pid
                order.original_bag = json.dumps(bag)
                if 'disc_code_readonly' in request.POST:
                    order.discount_code = request.POST['disc_code_readonly']
                order.save()

                for item_id, frame_detail in bag.items():
                    artwork_id = item_id.split('-')[0]
                    artwork = get_object_or_404(Artwork, pk=artwork_id)
                    frame = get_object_or_404(ArtFrame,
                                              pk=list(frame_detail['frame_id']
                                                      .keys())[0])
                    quantity = list(frame_detail['frame_id'].values())[0]
                    artwork_price = artwork.price
                    if artwork.on_sale:
                        artwork_price = artwork.get_sale_price()

                    order_line_item = OrderLineItem(
                        order=order,
                        artwork=artwork,
                        frame=frame,
                        quantity=quantity,
                        frame_price=frame.price,
                        artwork_price=artwork_price,
                    )
                    order_line_item.save()
                request.session['save_info'] = 'save-info' in request.POST
                return redirect(reverse('checkout_success',
                                args=[order.order_number]))
            else:
                messages.error(request, 'There was an error with your form. \
                    Please double check your information.')

    else:
        # load existing customer data from profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                form = OrderForm(initial={
                    'first_name': profile.first_name,
                    'last_name': profile.last_name,
                    'email': profile.user.email,
                    'phone': profile.phone,
                    'country': profile.country,
                    'postal_code': profile.postal_code,
                    'town_city': profile.town_city,
                    'street_address1': profile.street_address1,
                    'street_address2': profile.street_address2,
                    'county_region': profile.county_region,
                })
            except UserProfile.DoesNotExist:
                form = OrderForm()
        else:
            form = OrderForm()
    stripe.api_key = stripe_secret_key
    total = bag_content['grand_total']
    stripe_total = round(total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    context = {
        'form': form,
        'current_grand_total': current_grand_total,
        'discount': discount,
        'discount_code': discount_code,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def _get_discount(request, discount_code, order_total):
    # check if there is discount coupon
    discount = 0
    if discount_code:
        if not request.user.is_authenticated:
            return -2
        threshold_code = get_object_or_404(SystemPreference,
                                           code='CR').data
        threshold_per = Decimal(get_object_or_404(
                                SystemPreference, code='C2').data)
        threshold_amt = Decimal(get_object_or_404(
                                SystemPreference, code='T1').data)
        welcome_code = get_object_or_404(SystemPreference,
                                         code='CF').data
        welcome_per = Decimal(get_object_or_404(
                                SystemPreference, code='C1').data)

        if discount_code == welcome_code:
            # check if the code has been used before
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                if not profile.used_welcome_coupon:
                    discount = Decimal(welcome_per/100
                                       * order_total)
                else:
                    discount = -9
        elif discount_code == threshold_code:
            if order_total >= threshold_amt:
                discount = Decimal(threshold_per/100
                                   * order_total)
            else:
                discount = -1
    return discount


def checkout_success(request, order_number):
    """
    Feedback on successful checkouts
    and update profile if indicated by user
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {

                'first_name': order.first_name,
                'last_name': order.last_name,
                'phone': order.phone,
                'country': order.country,
                'postal_code': order.postal_code,
                'town_city': order.town_city,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'county_region': order.county_region,
            }
            profile_form = UserProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save(request)

    messages.success(request, f'Order was successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    if 'bag' in request.session:
        del request.session['bag']

    return render(request, 'checkout/checkout_success.html',
                  {
                    'order': order,
                  })


@require_POST
def cache_stripe_checkout_data(request):
    """ Pass additional data to stripe payment intent """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            'discount_code': request.POST.get('disc_code'),
        })
        return HttpResponse(status=200)
    except Exception as ex:
        print(ex)
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=ex, status=400)


@login_required
def customer_order_history(request):
    """ Display customers order history """

    orders = query_order(request, 'customer_order_history')
    if orders.count() > 0:
        orders = orders.filter(user_profile__user=request.user)
    query_dict = request.session.get("customer_order_history")

    paginator = Paginator(orders, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'checkout/customer_order_history.html',
                  {
                    'orders': page_obj,
                    'query_dict': query_dict,
                  })


@login_required
def order_details_list(request):
    """ Display all customers order history """

    # check that user is administrator/operator
    rights = check_in_group(request.user, ("administrator", "operator"))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    orders = query_order(request, 'order_details_enquiry')
    query_dict = request.session.get("order_details_enquiry")

    paginator = Paginator(orders, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'checkout/order_details_list.html',
                  {
                    'orders': page_obj,
                    'query_dict': query_dict,
                  })


@login_required
def update_order_status(request):
    """ Update order status """

    # check that user is administrator/operator
    rights = check_in_group(request.user, ("administrator", "operator"))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    edit_order = {'delivery': "",
                  'order_total': "",
                  'discount': "",
                  'grand_total': "",
                  'order_number': "",
                  'email': "",
                  'status': "",
                  }

    if request.method == "POST":
        if 'select-btn' in request.POST:
            order = Order.objects.get(
                    order_number=request.POST.get('select-btn'))
            edit_order = {'delivery': order.delivery_cost,
                          'order_total': order.order_total,
                          'discount': order.discount,
                          'grand_total': order.grand_total,
                          'order_number': order.order_number,
                          'email': order.email,
                          'status': order.status.code,
                          }
        elif 'confirm-action-btn' in request.POST:
            # for update after user confirms the update prompt
            order = Order.objects.get(
                    order_number=request.POST.get('confirm-id'))
            status = get_object_or_404(
                     OrderStatus, code=request.POST.get('new_order_status'))
            if order.status.code == status.code:
                messages.warning(request, "You choose same status as before.\
                     Select a different status and try again")
            else:
                order.status = status
                order.save()

                # Write notification record
                if order.user_profile:
                    message = "The status of your Order number "
                    message += f"{order.order_number} has changed to \
                        {order.status}"
                    Notification.objects.create(
                        subject="Order Status Change #: " + order.order_number,
                        message=message,
                        user=order.user_profile)

                messages.success(request, f"The order status for \
                    {order.order_number} has been updated successfully \
                        to {status.description}")

    orders = query_order(request, 'update_order_status')
    query_dict = request.session.get("update_order_status")

    paginator = Paginator(orders, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'checkout/update_order_status.html',
                  {
                    'orders': page_obj,
                    'query_dict': query_dict,
                    'edit_order': edit_order,
                  })


@login_required
def view_notification(request):
    """ Display/delete customers notifications """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    notices = Notification.objects.filter(user=user_profile).order_by(
                                          '-notice_date')
    if notices.count() > 0:
        subject = notices[0].subject
        message = notices[0].message
    else:
        subject = ""
        message = ""
    if request.method == "POST":
        if 'select-rec' in request.POST:
            rec_id = request.POST.get('select-rec')
            select_notice = get_object_or_404(Notification, id=rec_id)
            subject = select_notice.subject
            message = select_notice.message
        elif 'confirm-action-btn' in request.POST:
            # from delete action
            id_sent = request.POST.get('confirm-id')
            select_notice = get_object_or_404(Notification, id=id_sent)
            subj = select_notice.subject
            select_notice.delete()
            messages.success(request,
                             ('Message with subject: ' + subj +
                              ' was successfully deleted!'))

    paginator = Paginator(notices, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'checkout/notifications.html',
                  {
                    'notices': page_obj,
                    'subject': subject,
                    'message': message,
                  })


def request_order_return(request):
    """ Request return of an order if its within the acceptable period
        The order number or email address is used to retrieve the order
        since there could be anonymous users
        """
    form = ReturnOrderForm()
    orders = None
    if request.method == 'POST':
        orders = query_order(request, 'request_order_return')
    if orders.count() > 0:
        orders.filter(status__code='O')
    # query_dict = request.session.get("request_order_return")

    return render(request, 'checkout/request_return_order.html',
                  {
                    'orders': orders,
                    'form': form,
                  })
