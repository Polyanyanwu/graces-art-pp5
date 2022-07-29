""" Admin config and for artworks tables """

from django.contrib import admin
from .models import Artist, ArtGenre, ArtStyle


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    ''' Maintain Artist '''
    model = Artist
    list_display = ('pk', 'name', 'friendly_name', )


@admin.register(ArtGenre)
class ArtGenreAdmin(admin.ModelAdmin):
    ''' Maintain Art genre '''
    model = ArtGenre
    list_display = ('pk', 'name', 'friendly_name', )


@admin.register(ArtStyle)
class ArtStyleAdmin(admin.ModelAdmin):
    ''' Maintain ArtStyle '''
    model = ArtStyle
    list_display = ('pk', 'name', 'friendly_name', )
