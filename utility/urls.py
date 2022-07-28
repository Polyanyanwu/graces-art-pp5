""" URLs for utility tables maintenance """
from django.urls import path
from . import views


urlpatterns = [
    path('sys_pref/', views.SystemPreferenceView.as_view(),
         name='system_preference'),
    path('info/', views.HomeMessageView.as_view(),
         name='general_info'),
]
