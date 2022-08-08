""" Module to process checkout and payment """

from decimal import Decimal
import json
import stripe
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST

from bag.contexts import bag_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from utility.models import SystemPreference
from artworks.models import Artwork, ArtFrame
from .models import OrderLineItem, Order
from .forms import OrderForm


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
    # print(intent)
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
