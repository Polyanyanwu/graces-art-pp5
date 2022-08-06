""" Urls for the Artworks app """

from django.urls import path
from . import views


urlpatterns = [
    path('<int:artwork_id>/', views.add_to_bag, name='add_to_bag'),
    path('vb', views.view_bag, name='view_bag'),
    path('ub', views.update_bag, name='update_bag'),
]
