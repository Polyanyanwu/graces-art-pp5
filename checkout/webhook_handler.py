"""
Stripe webhooks handler: if checkout fails,
the webhook handler executes all the expected functions.
(payment processing, send email, save order and profile info)
"""

import json
import time
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

from artworks.models import Artwork, ArtFrame
from profiles.models import UserProfile
from .models import Order, OrderLineItem


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
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        discount_code = intent.metadata.discount_code
        # No discount is sent as X from the javascript
        if discount_code == "X":
            discount_code = None

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        if shipping_details.phone == "":
            shipping_details["phone"] = None

        # Extract first name and last name

        names = shipping_details.name.split(":")
        first_name = last_name = None
        if len(names[0].strip()) > 0:
            first_name = names[0].strip()
        if len(names[1].strip()) > 0:
            last_name = names[1].strip()

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.first_name = first_name
                profile.last_name = last_name
                profile.phone = shipping_details.phone
                profile.country = shipping_details.address.country
                profile.postal_code = shipping_details.address.postal_code
                profile.town_city = shipping_details.address.city
                profile.street_address1 = shipping_details.address.line1
                profile.street_address2 = shipping_details.address.line2
                profile.county_region = shipping_details.address.state
                profile.save()

        # Check if Order already exists
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=first_name,
                    last_name__iexact=last_name,
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postal_code__iexact=shipping_details.address.postal_code,
                    town_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county_region__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    discount_code=discount_code,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_email_confirmation(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS:\
                     Verified order already in the database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    postal_code=shipping_details.address.postal_code,
                    town_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county_region=shipping_details.address.state,
                    discount_code=discount_code,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, frame_detail in json.loads(bag).items():
                    artwork_id = item_id.split('-')[0]

                    artwork = Artwork.objects.get(id=artwork_id)
                    frame = ArtFrame.objects.get(
                            id=list(frame_detail['frame_id'].keys())[0])
                    quantity = list(frame_detail['frame_id'].values())[0]

                    if artwork.on_sale:
                        artwork_price = artwork.get_sale_price()
                    else:
                        artwork_price = artwork.price
                    order_line_item = OrderLineItem(
                        order=order,
                        artwork=artwork,
                        quantity=quantity,
                        frame=frame,
                        frame_price=frame.price,
                        artwork_price=artwork_price,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_email_confirmation(order)
        return HttpResponse(
            content=f'Webhook received {event["type"]} | \
                      SUCCESS: Created in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook from stripe """
        return HttpResponse(
            content=f'Payment failed Webhook received {event["type"]}',
            status=200)
