""" URL Configuration for home app """


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('coupon', views.coupons, name='coupons'),
    path('contact', views.contact_us, name='contact_us'),
]
