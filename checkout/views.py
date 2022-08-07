""" Module to process checkout and payment """

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('get_artworks'))
    form = OrderForm()
    template = 'checkout/checkout.html'
    if request.method == 'POST':
        print(request.POST)
    context = {
        'form': form,
    }

    return render(request, template, context)
