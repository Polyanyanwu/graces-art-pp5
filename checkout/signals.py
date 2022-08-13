"""
Signals that listen for the creation or deletion of an OrderLineItem
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem, ReturnOrder, CancelOrder


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total for each line item update/create event """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ Update order total for each line item delete event """
    instance.order.update_total()


@receiver(post_save, sender=ReturnOrder)
def email_on_save(sender, instance, created, **kwargs):
    """ Send email acknowledgement when customer
        requests to return order
    """
    if created:
        instance.send_return_request_email()


@receiver(post_save, sender=CancelOrder)
def email_on_cancel_order(sender, instance, created, **kwargs):
    """ Send email acknowledgement when customer
        cancels an order
    """
    if created:
        instance.send_cancel_confirm_email()
