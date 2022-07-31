""" Forms for Artwork Module """

from django import forms
from .models import Artist, ArtStyle, ArtGenre, Artwork


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


class ArtworkForm(forms.ModelForm):
    """ New artwork Form"""

    class Meta:
        """ New Artwork Meta """
        model = Artwork
        fields = ('name', 'artist', 'genre', 'style', 'sku', 'on_sale', 'price', 'rating', 'image_url', 'image')
