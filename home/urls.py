""" URL Configuration for home app """


from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('coupon', views.coupons, name='coupons'),
    path('contact', views.contact_us, name='contact_us'),
    path('write_review', login_required(views.WriteReviewView.as_view()),
         name='write_review'),
    path('review', views.view_reviews, name='reviews'),
]
