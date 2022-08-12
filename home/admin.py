""" Admin for contact us form
    if time doesn't permit to bring t to the UI
"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ContactUs, FAQ


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    ''' Maintain Contact messages list '''
    model = ContactUs
    list_display = ('date_time', 'subject', 'sender', 'message_body', 'user', )
    search_fields = ['subject', 'message_body']
    list_filter = ('subject', )


@admin.register(FAQ)
class FAQAdmin(SummernoteModelAdmin):
    ''' Maintain FAQ  '''
    model = FAQ
    list_display = ('last_view_date', 'question')
    search_fields = ['question']
    list_filter = ('question', )
    summernote_fields = ('explanation',)
