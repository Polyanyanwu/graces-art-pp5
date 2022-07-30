""" Forms for Artwork Module """

from django import forms
from .models import Artist, ArtStyle


class ArtistForm(forms.ModelForm):
    """ Artist form """
    class Meta:
        """ Meta for Artist Form """
        model = Artist
        fields = '__all__'


class ArtStyleForm(forms.ModelForm):
    """ Art Style form """
    class Meta:
        """ Meta for Artist Form """
        model = ArtStyle
        fields = '__all__'
