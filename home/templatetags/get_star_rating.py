""" template tag for ratings
    enables me to produce display of stars for ratings
    on templates
"""
import math
from django import template

register = template.Library()


@register.filter(name='rating_main')
def get_main_rating(rating):
    """ Template tag used to return number of ratings
    """
    return range(rating)


@register.filter(name='rating_bal')
def get_rating_balance(rating):
    """ Template tag used to return the rating minus 5
        integer rating
    """
    return range(5-rating)


@register.filter(name='rating_dec_main')
def get_dec_main_rating(rating):
    """ Template tag used to return number of ratings
        for decimal values
    """
    num = math.modf(rating)
    return range(int(num[1]))


@register.filter(name='rating_dec_bal')
def get_dec_bal_rating(rating):
    """ Template tag used to return number of ratings
        for decimal values
    """
    num = math.modf(rating)
    if num[0] > 0:
        return range(4-int(num[1]))
    else:
        return range(5-int(num[1]))


@register.filter(name='rating_dec_fraction')
def get_dec_fraction_rating(rating):
    """ Template tag used to return number of ratings
        for decimal values fraction
    """
    num = math.modf(rating)
    if num[0] > 0:
        return True
    else:
        return False
