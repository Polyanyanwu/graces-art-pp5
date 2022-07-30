""" Forms for Artwork Module """

from django import forms
from .models import Artist, ArtStyle, ArtGenre


class ArtistForm(forms.ModelForm):
    """ Artist form """
    class Meta:
        """ Meta for Artist Form """
        model = Artist
        fields = '__all__'


class ArtStyleForm(forms.ModelForm):
    """ Art Style form """
    class Meta:
        """ Meta for Art Style Form """
        model = ArtStyle
        fields = '__all__'


class ArtGenreForm(forms.ModelForm):
    """ Art Genre form """
    class Meta:
        """ Meta for Art Genre Form """
        model = ArtGenre
        fields = '__all__'
