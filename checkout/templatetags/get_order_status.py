""" template tag for getting order status """

from django import template

register = template.Library()


@register.filter(name='order_status')
def get_order_status(code):
    """ Template tag used to get descriptive order status
    """
    if code == "O":
        return "Ordered"
    elif code == "R":
        return "Returned"
    elif code == "F":
        return "Fulfilled"
    elif code == "C":
        return "Cancelled"
