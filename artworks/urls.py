""" Urls for the Artworks app """

from django.urls import path
from . import views


urlpatterns = [
    path('artist', views.maintain_artist, name='maintain_artists'),
]
