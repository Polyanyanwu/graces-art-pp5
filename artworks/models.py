""" Artwork and related tables model """

from django.db import models


class Artist(models.Model):
    """ Artists that created artworks"""
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        """ Verbose name of table"""
        verbose_name_plural = 'Artists'

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """ Get the friendly name for display"""
        return self.friendly_name


class ArtStyle(models.Model):
    """ Art Styles for the artworks"""
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        """ Verbose name of table"""
        verbose_name_plural = 'ArtStyles'

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """ Get the friendly name for display"""
        return self.friendly_name


class ArtGenre(models.Model):
    """ Art Genre for the artworks"""
    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        """ Verbose name of table"""
        verbose_name_plural = 'ArtGenres'

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """ Get the friendly name for display"""
        return self.friendly_name
