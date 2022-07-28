""" Forms for the System Preferences and Home message
    THe home message table is used to store the Terms of Use
    and Privacy Notice
"""
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField
from .models import SystemPreference, HomeMessage


class SystemPreferenceForm(forms.ModelForm):
    """ Update system preferences data """
    class Meta:
        """ Specify the model to update """
        model = SystemPreference
        fields = ('code', 'data', 'data_type')
        readonly_fields = ('code', 'data_type')


class HomeMessageForm(forms.ModelForm):
    """ Privacy Notice and Terms of Use data """
    description = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = HomeMessage

        # description = SummernoteTextField()
        fields = ('code', 'description')

# class FormFromSomeModel(forms.ModelForm):
#     class Meta:
#         model = SomeModel
#         widgets = {
#             'foo': SummernoteWidget(),
#             'bar': SummernoteInplaceWidget(),
#         }