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
        fields = ('id', 'name', 'artist', 'genre', 'style', 'sku', 'on_sale',
                  'price', 'rating', 'image_url', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # display friendly names for artists dropdown sorted
        artists = Artist.objects.all()
        friendly_names = [(a.id, a.get_friendly_name()) for a in artists]
        friendly_names.append(('--', '-'))
        sorted_friendly_names = sorted((trans for trans in friendly_names),
                                       key=lambda x: x[1])
        self.fields['artist'].choices = sorted_friendly_names

        # display friendly names for Genre dropdown
        genres = ArtGenre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genres]
        friendly_names.append(('--', '-'))
        sorted_friendly_names = sorted((trans for trans in friendly_names),
                                       key=lambda x: x[1])
        self.fields['genre'].choices = sorted_friendly_names

        # display friendly names for Style dropdown
        styles = ArtStyle.objects.all()
        friendly_names = [(s.id, s.get_friendly_name()) for s in styles]
        friendly_names.append(('--', '-'))
        sorted_friendly_names = sorted((trans for trans in friendly_names),
                                       key=lambda x: x[1])
        self.fields['style'].choices = sorted_friendly_names
