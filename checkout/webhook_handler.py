"""
Stripe webhooks handler: if checkout fails,
the webhook handler executes all the expected functions.
(payment processing, send email, save order and profile info)
"""

from django.http import HttpResponse


class StripeWebhookHandler:
    """ Handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook received {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeed webhook from stripe """
        intent = event.data.object
        print("at event success", intent)
        return HttpResponse(
            content=f'Webhook received {event["type"]} | \
                      SUCCESS: Created in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook from stripe """
        return HttpResponse(
            content=f'Payment failed Webhook received {event["type"]}',
            status=200)
