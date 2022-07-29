""" Urls for the profiles app """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.update_profile, name='update_profile'),
    path('role', views.update_group, name='update_group'),
]
