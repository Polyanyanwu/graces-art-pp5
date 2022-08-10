""" template tag for getting order status """

from django import template
from checkout.models import OrderStatus

register = template.Library()


@register.filter(name='order_status')
def get_order_status(code):
    """ Template tag used to get all order status
    """
    return OrderStatus.objects.all()

