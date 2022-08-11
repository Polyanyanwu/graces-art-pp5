""" Admin module for orders """

from django.contrib import admin
from .models import Order, OrderLineItem, OrderStatus, Notification, ReturnOrder


class OrderLineItemAdminInline(admin.TabularInline):
    """ Line item model """
    model = OrderLineItem
    readonly_fields = ('line_item_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Order model """
    model = Order
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total', 'discount',
                       'grand_total', 'original_bag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'first_name',
              'last_name', 'email', 'phone', 'country',
              'postal_code', 'town_city', 'street_address1',
              'street_address2', 'county_region', 'delivery_cost',
              'discount', 'discount_code', 'order_total', 'grand_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'first_name',
                    'order_total', 'delivery_cost', 'discount',
                    'grand_total',)

    ordering = ('-date',)


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    """ Order Status model """
    model = OrderStatus
    fields = ('code', 'description')
    list_display = ('code', 'description')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """ Notification model """
    model = Notification
    fields = ('subject', 'message', 'user')
    list_display = ('notice_date', 'subject', 'user')


@admin.register(ReturnOrder)
class ReturnOrderAdmin(admin.ModelAdmin):
    """ Return Order model """
    model = ReturnOrder
    # fields = '__all__'
    # list_display = ('notice_date', 'subject', 'user')