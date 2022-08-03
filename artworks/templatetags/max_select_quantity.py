""" template tag for getting maximum quantity """

from django import template
from django.shortcuts import get_object_or_404
from utility.models import SystemPreference

register = template.Library()


@register.filter(name='max_qty')
def get_maximum_qty():
    """ Template tag used to get the maximum quantity of an
    artwork that a customer can input
    """
    max_qty_rec = get_object_or_404(SystemPreference, code='Q')
    return int(max_qty_rec.data)
