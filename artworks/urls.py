""" Urls for the Artworks app """

from django.urls import path
from . import views


urlpatterns = [
    path('artist', views.maintain_artist, name='maintain_artists'),
    path('artstyle', views.maintain_art_style, name='maintain_art_style'),
    path('artgenre', views.maintain_art_genre, name='maintain_art_genre'),
    path('shop', views.get_artworks, name='get_artworks'),
    path('add', views.add_artwork, name='add_artwork'),
]
