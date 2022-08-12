""" Models for the bag app"""

from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork


class WishList(models.Model):
    """ Model to maintain wishlist for logged in users """
    artwork = models.ForeignKey(Artwork, on_delete=models.SET_NULL,
                                null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artwork.name
