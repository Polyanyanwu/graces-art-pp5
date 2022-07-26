""" Urls for the Checkout app """

from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('payment_success/<order_number>', views.checkout_success,
         name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path('cache_stripe_checkout_data/', views.cache_stripe_checkout_data,
         name='cache_stripe_checkout_data'),
    path('customer_history/', views.customer_order_history,
         name='customer_order_history'),
    path('order_details/', views.order_details_list,
         name='order_details_list'),
    path('order_status/', views.update_order_status,
         name='update_order_status'),
    path('notice/', views.view_notification,
         name='view_notification'),
    path('return_request/', views.request_order_return,
         name='request_order_return'),
    path('review_order_return/', views.review_order_return,
         name='review_order_return'),
    path('cancel_order', views.request_cancel_order,
         name='cancel_order'),
]
