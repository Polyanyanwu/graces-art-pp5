""" Module to process checkout and payment """

from decimal import Decimal
from datetime import datetime, timezone
import json
import stripe
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.mail import send_mail

from bag.contexts import bag_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from profiles.user_belong import check_in_group
from utility.models import SystemPreference
from artworks.models import Artwork, ArtFrame
from .models import (
    OrderLineItem, Order, OrderStatus,
    CancelOrder, Notification, ReturnOrder)
from .forms import OrderForm, ReturnOrderForm, CancelOrderForm
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


@login_required
def request_order_return(request):
    """ Request return of an order if its within the acceptable period
        The order number or email address is used to retrieve the order
    """
    form = ReturnOrderForm()
    form_order_num = ""
    form_order_total = ""
    form_order_delivery = ""
    form_order_grand = ""
    form_order_discount = ""

    if request.method == 'POST':
        if 'select-btn' in request.POST:
            order_num = request.POST.get('select-btn')
            f_order = get_object_or_404(Order, order_number=order_num)
            existing_req = ReturnOrder.objects.filter(
                order=f_order).order_by('-request_date')
            # check if the order date is within allowed return date
            return_days = int(get_object_or_404(
                              SystemPreference, code="R").data)
            now = datetime.now(timezone.utc)
            order_date = f_order.date
            delta = (now - order_date).days
            date_str = f_order.date.strftime("%d-%b-%Y %H:%M")
            if delta > return_days:
                messages.error(request, f"Sorry you can no longer request \
                    for return of this order placed on {date_str}. \
                        You had within {return_days} days to do so")
            elif existing_req.count() > 0:
                d_str = existing_req[0].request_date.strftime("%d-%b-%Y %H:%M")
                messages.error(request, f"Sorry you have an existing request \
                    to return this order. Request was on {d_str}. \
                        You will soon hear from us")
            else:
                form_order_total = f_order.order_total
                form_order_delivery = f_order.delivery_cost
                form_order_discount = f_order.discount
                form_order_grand = f_order.grand_total
                form_order_num = order_num
                form = ReturnOrderForm(initial={'order': f_order.order_number})

    if 'confirm-action-btn' in request.POST:
        # save confirmation
        form = ReturnOrderForm(data=request.POST)
        if form.is_valid():
            order_num = request.POST.get('form-order-no')
            return_rec = form.save(commit=False)
            return_order = get_object_or_404(Order, order_number=order_num)
            user = UserProfile.objects.get(user=request.user)
            return_rec.order = return_order
            return_rec.user = user
            return_rec.save()
            messages.success(request, "Your request has been sent. An email \
                will be sent to your registered email address with us!")

    orders = query_order(request, 'request_order_return')
    if orders.count() > 0:
        orders = orders.filter(Q(user_profile__user=request.user) &
                               Q(status__code='R'))

    query_dict = request.session.get("request_order_return")
    paginator = Paginator(orders, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'checkout/request_return_order.html',
                  {
                    'orders': page_obj,
                    'form': form,
                    'query_dict': query_dict,
                    'form_order_num': form_order_num,
                    'form_order_total': form_order_total,
                    'form_order_delivery': form_order_delivery,
                    'form_order_discount': form_order_discount,
                    'form_order_grand': form_order_grand,
                  })


@login_required
def review_order_return(request):
    """ Review request to return order
        Approve or reject only operator/admin
    """
    # check that user is administrator/operator
    rights = check_in_group(request.user, ("administrator", "operator"))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    return_req = None
    return_order = None

    if request.method == 'POST':
        if 'select-btn' in request.POST:
            order_num = request.POST.get('select-btn')
            return_order = get_object_or_404(Order, order_number=order_num)
            return_qs = ReturnOrder.objects.filter(order=return_order)
            if return_qs.count() > 0:
                return_req = return_qs[0]
                if return_req.approved is not None:
                    # it has been reviewed before
                    messages.warning(request, "This request has been reviewed! \
                        Please change the status when shipped or delivered")
                    return_req = None
                    return redirect("review_order_return")          
            else:
                # maybe the status was changed not by customer
                messages.warning(request, "No customer request data exits!")
                return redirect("review_order_return")

        if 'confirm-action-btn' in request.POST:
            # confirm rejection of request
            order_num = request.POST.get('confirm-id')
            if not order_num:
                messages.warning(request, "Please select an order first")
                return redirect("review_order_return")
            else:
                return_rec = get_object_or_404(
                             ReturnOrder, order__order_number=order_num)
                return_order = get_object_or_404(Order, order_number=order_num)
                user = UserProfile.objects.get(user=request.user)
                return_rec.reviewed_by = user
                return_rec.review_comments = request.POST.get(
                                             'review-comments')
                return_rec.approved = False
                return_rec.save()
                # set the status back to Ordered
                status = get_object_or_404(OrderStatus, code="O")
                return_order.status = status
                return_order.save()

                # send email confirmation
                send_to = return_rec.user.user.email
                subject = 'Rejection of Return Order: '\
                    + return_order.order_number
                body = render_to_string(
                    'checkout/email_template/return_request_decision.txt',
                    {'order': return_order,
                     'return_rec': return_rec,
                     'decision': 'Not Approved'})
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [send_to]
                )

                # Write notification record
                Notification.objects.create(
                    subject=subject + ": " + return_order.user_profile.get_fullname(),
                    message=body,
                    user=return_order.user_profile)

                return_order = None
                messages.success(request, "Your rejection of the request has \
                    been saved. An email will be sent to the customer!")

        if 'approve-btn' in request.POST:
            order_num = request.POST.get('approve-btn')
            if not order_num:
                messages.warning(request, "Please select an order first")
                return redirect("review_order_return")
            else:
                return_rec = get_object_or_404(
                             ReturnOrder, order__order_number=order_num)
                return_order = get_object_or_404(Order, order_number=order_num)
                user = UserProfile.objects.get(user=request.user)
                return_rec.reviewed_by = user
                return_rec.approved = True
                return_rec.review_comments = request.POST.get(
                                             'review-comments')
                return_rec.save()
                # status remains are Returned until changed to shipped later

                # send email confirmation
                send_to = return_rec.user.user.email
                subject = 'Approval of Return Order: '\
                    + return_order.order_number
                body = render_to_string(
                    'checkout/email_template/return_request_decision.txt',
                    {'order': return_order,
                     'return_rec': return_rec,
                     'decision': 'Approved'})
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [send_to]
                )

                # Write notification record
                Notification.objects.create(
                    subject=subject + ": " + return_order.user_profile.get_fullname(),
                    message=body,
                    user=return_order.user_profile)
                return_order = None
                messages.success(request, "Your approval of the request has \
                    been saved. An email will be sent to the customer!")

    orders = query_order(request, 'review_order_return')
    if orders.count() > 0:
        orders = orders.filter(
            Q(return_order__approved=None) &
            Q(status__code='R'))

    query_dict = request.session.get("review_order_return")
    paginator = Paginator(orders, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'checkout/review_order_return.html',
                  {
                    'orders': page_obj,
                    'query_dict': query_dict,
                    'return_order': return_order,
                    'return_req': return_req,
                  })


@login_required
def request_cancel_order(request):
    """ Request cancel of an order if its within the acceptable period
        The order number or email address is used to retrieve the order
    """
    form = CancelOrderForm()
    form_order_num = ""
    form_order_total = ""
    form_order_delivery = ""
    form_order_grand = ""
    form_order_discount = ""

    if request.method == 'POST':
        if 'select-btn' in request.POST:
            order_num = request.POST.get('select-btn')
            f_order = get_object_or_404(Order, order_number=order_num)
            existing_req = CancelOrder.objects.filter(
                order=f_order).order_by('-date')
            # check if the order date is within allowed return date
            return_days = int(get_object_or_404(
                              SystemPreference, code="C").data)
            print("cancel days==", return_days, " date==", f_order.date)
            now = datetime.now(timezone.utc)
            order_date = f_order.date
            delta = (now - order_date).days
            print("date diff===", delta)
            date_str = f_order.date.strftime("%d-%b-%Y %H:%M")
            if delta > return_days:
                messages.error(request, f"Sorry you can no longer cancel \
                    this order placed on {date_str}. \
                        You had within {return_days} days to do so")
            elif existing_req.count() > 0:
                d_str = existing_req[0].date.strftime("%d-%b-%Y %H:%M")
                messages.error(request, f"Sorry you have already cancelled \
                    this order. Request was on {d_str}.")
            else:
                form_order_total = f_order.order_total
                form_order_delivery = f_order.delivery_cost
                form_order_discount = f_order.discount
                form_order_grand = f_order.grand_total
                form_order_num = order_num
                form = CancelOrderForm(initial={'order': f_order.order_number})

    if 'confirm-action-btn' in request.POST:
        # save confirmation
        form = CancelOrderForm(data=request.POST)
        if form.is_valid():
            order_num = request.POST.get('form-order-no')
            cancel_rec = form.save(commit=False)
            cancel_order = get_object_or_404(Order, order_number=order_num)
            user = UserProfile.objects.get(user=request.user)
            cancel_rec.order = cancel_order
            cancel_rec.user = user
            cancel_rec.save()
            messages.success(request, "Your order has been cancelled. An email \
                has been sent to your registered email address with us!")

    orders = query_order(request, 'cancel_order')
    if orders.count() > 0:
        orders = orders.filter(Q(user_profile__user=request.user) &
                               Q(status__code='O')).order_by('-date')

    query_dict = request.session.get("cancel_order")
    paginator = Paginator(orders, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'checkout/cancel_order.html',
                  {
                    'orders': page_obj,
                    'form': form,
                    'query_dict': query_dict,
                    'form_order_num': form_order_num,
                    'form_order_total': form_order_total,
                    'form_order_delivery': form_order_delivery,
                    'form_order_discount': form_order_discount,
                    'form_order_grand': form_order_grand,
                  })
