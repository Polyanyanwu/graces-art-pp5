""" Models for storing orders """

import uuid

from django.db import models
from django.db.models import Sum
from decimal import Decimal
from django_countries.fields import CountryField

from artworks.models import Artwork, ArtFrame
from profiles.models import UserProfile
from utility.models import SystemPreference


class Order(models.Model):
    """ Model that for storing orders from customers """

    STATUS_CHOICES = [
            ('O', 'Ordered'),
            ('F', 'Fulfilled'),
            ('R', 'Returned'),
        ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    town_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county_region = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2,
                                        null=False, default=0)
    discount = models.DecimalField(max_digits=8, decimal_places=2,
                                   null=False, default=0)
    discount_code = models.CharField(max_length=15, null=True, blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES, default="O")

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.line_items.aggregate(
                           Sum('line_item_total'))['line_item_total__sum'] or 0

        self.delivery_cost = Decimal(int(get_object_or_404(SystemPreference,
                                code='DP').data) * self.order_total / 100)
        max_delivery_cost = Decimal(get_object_or_404(SystemPreference,
                                    code='DC').data)
        if self.delivery_cost > max_delivery_cost:
            self.delivery_cost = max_delivery_cost

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='line_items')
    artwork = models.ForeignKey(Artwork, null=False, blank=False,
                                on_delete=models.CASCADE)
    frame = models.ForeignKey(ArtFrame, null=False, blank=False,
                              on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_item_total = models.DecimalField(max_digits=8,
                                          decimal_places=2, null=False,
                                          blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line_item total
        and update the order total.
        """

        if self.artwork.on_sale:
            sale_price = float(self.artwork.get_sale_price())
            self.line_item_total = self.quantity * (Decimal(sale_price)
                                                    + self.frame.price)
        else:
            self.line_item_total = Decimal(self.quantity *
                                           (self.artwork.price
                                            + self.frame.price))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.artwork.sku} on order {self.order.order_number}'


class ReturnOrder(models.Model):
    """ Model to store order return entry and approval details """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='return_order')
    reason = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, blank=True,
                             related_name='request_user')
    request_date = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name='review_user')
    approved = models.BooleanField(null=True, blank=True)
    date_approved = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.order.order_number}'
