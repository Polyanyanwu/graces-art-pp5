""" Forms for Artwork Module """

from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    """ Artist form """
    class Meta:
        """ Meta for Artist Form """
        model = Artist
        fields = '__all__'
