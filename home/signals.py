"""
Signals that listen for contact message to send email reply
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ContactUs


@receiver(post_save, sender=ContactUs)
def send_email_confirm_for_contact_us(sender, instance, created, **kwargs):
    """ Send email confirmation when user contacts successfully"""

    if created:
        instance.send_contact_message()
