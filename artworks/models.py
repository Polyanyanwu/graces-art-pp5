""" Artwork and related tables model """

from django.db import models
from django.core.validators import \
    (MinLengthValidator, MinValueValidator, MaxValueValidator)
from utility.models import SystemPreference


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


class Artwork(models.Model):
    """ Artwork to be selected by user """

    sku = models.CharField(max_length=50, null=True, blank=True,
                           unique=True,
                           validators=[MinLengthValidator(12), ])
    name = models.CharField(max_length=254)
    artist = models.ForeignKey('Artist', null=True, blank=True,
                               on_delete=models.SET_NULL)
    genre = models.ForeignKey('ArtGenre', null=True, blank=True,
                              on_delete=models.SET_NULL)
    style = models.ForeignKey('ArtStyle', null=True, blank=True,
                              on_delete=models.SET_NULL)
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    sale_percentage = models.ForeignKey(SystemPreference, null=True,
                                        blank=True, on_delete=models.SET_NULL,
                                        default="S")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=5, decimal_places=2,
                                 validators=[MaxValueValidator(5),
                                             MinValueValidator(0)],
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_sale_price(self):
        """ Calculate and return sale price from settings
        in the System Preference """
        if self.sale_percentage.data:
            sales_per = int(self.sale_percentage.data)
            return self.price * sales_per/100
        else:
            return self.price


class ArtFrame(models.Model):
    """ Artframe to be selected by user """

    name = models.CharField(max_length=254, null=False, blank=False)
    size = models.CharField(max_length=10, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(1)])
    qty = models.PositiveIntegerField(null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
