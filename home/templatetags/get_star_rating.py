""" template tag for ratings """

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
    """
    return range(5-rating)
