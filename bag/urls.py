""" Urls for the Artworks app """

from django.urls import path
from . import views


urlpatterns = [
    path('<int:artwork_id>/', views.add_to_bag, name='add_to_bag'),
]
