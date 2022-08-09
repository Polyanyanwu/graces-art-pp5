"""
Stripe webhooks handler: if checkout fails,
the webhook handler executes all the expected functions.
(payment processing, send email, save order and profile info)
"""

from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail


class StripeWebhookHandler:
    """ Handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def _send_email_confirmation(self, order):
        """Send the user a confirmation email"""
        customer_email = order.email
        subject = render_to_string(
            'checkout/email_template/order_confirm_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/email_template/order_confirm_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        """ Handle generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook received {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeed webhook from stripe """
        intent = event.data.object
        print("at event success", intent)

        self._send_email_confirmation(order)
        return HttpResponse(
            content=f'Webhook received {event["type"]} | \
                      SUCCESS: Created in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook from stripe """
        return HttpResponse(
            content=f'Payment failed Webhook received {event["type"]}',
            status=200)
