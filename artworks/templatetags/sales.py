""" template tag for sale price """

# from django import template
# from utility.models import SystemPreference
# from django.shortcuts import render, get_object_or_404

# register = template.Library()


# @register.filter(name='sale_price')
# def get_sale_price(artwork):
#     """ Template tag used to get the sale price for an item on sale
#     """
#     sale_p = get_object_or_404(SystemPreference, code=artwork.sale_percentage)
#     price = artwork.price
#     sale_per = int(sale_p.data)
#     sale_amt = price - price * sale_per / 100
#     return sale_amt
