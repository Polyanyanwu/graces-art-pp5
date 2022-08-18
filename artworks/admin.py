""" Admin config and for artworks tables """

from django.contrib import admin
from .models import Artist, ArtGenre, ArtStyle, Artwork


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    ordering = ('sku',)
    list_display = ('sku', 'name', 'on_sale', 'sale_percentage')
