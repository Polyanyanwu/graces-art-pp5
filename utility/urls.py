""" URLs for utility tables maintenance """
from django.urls import path
from . import views


urlpatterns = [
     path('sys_pref/', views.SystemPreferenceView.as_view(),
          name='system_preference'),
     path('info/', views.HomeMessageView.as_view(),
          name='general_info'),
     path('terms/', views.terms_of_use, name='terms_of_use'),
     path('pp/', views.privacy_policy, name='privacy_policy'),
]
