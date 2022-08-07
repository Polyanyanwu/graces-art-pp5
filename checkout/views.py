""" Module to process checkout and payment """

from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from bag.contexts import bag_contents
from profiles.models import UserProfile
from utility.models import SystemPreference
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('get_artworks'))
    bag_content = bag_contents(request)
    current_grand_total = bag_content['grand_total']

    form = OrderForm()
    template = 'checkout/checkout.html'
    discount_code = None
    discount = 0
    if request.method == 'POST':
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
            current_grand_total -= discount
    context = {
        'form': form,
        'current_grand_total': current_grand_total,
        'discount': discount,
        'discount_code': discount_code,
    }

    return render(request, template, context)


def _get_discount(request, discount_code, order_total):
    # check if there is discount coupon
    discount = 0
    if discount_code:
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
            # check if he has used this code before
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
