""" Admin config and registration for general tables
    The summernote library was used to enable the superuser
    to input and maintain the Terms of Use and Privacy Notice
    for the site instead of hard coding it"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    SystemPreference, HomeMessage)


@admin.register(SystemPreference)
class BookingStatusAdmin(admin.ModelAdmin):
    ''' Maintain System Preference '''
    model = SystemPreference
    list_display = ('code', 'data', 'data_type', )


@admin.register(HomeMessage)
class HomeMessageAdmin(SummernoteModelAdmin):
    """ Maintain Text for Privacy policy & Terms of Use"""
    list_display = ('code', )
    summernote_fields = ('description',)
