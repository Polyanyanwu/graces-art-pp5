""" Urls for the Checkout app """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
]
