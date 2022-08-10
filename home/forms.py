""" Contact form for receiving contact us messages """
from django import forms
from .models import ContactUs, Review


class ContactUsForm(forms.ModelForm):
    """ Configure the contact us form """

    sender = forms.EmailField(label='Email Address',
                              widget=forms.TextInput(
                               attrs={'placeholder': 'Email address'}))

    class Meta:
        """ Form meta class """
        model = ContactUs
        fields = ('subject', 'sender', 'message_body')


class ReviewForm(forms.ModelForm):
    """ Configure the Review form """

    class Meta:
        """ Form meta class """
        model = Review
        fields = ('rating', 'message')
