""" Form testing class """
from django.test import TestCase
from .forms import ArtistForm


class TesItemForm(TestCase):
    """ Form testing class"""
    fixtures = ["test_fixture/artist.json"]

    def test_name_is_required(self):
        """ test artist name on the form is required """
        form = ArtistForm({'name': '', 'friendly_name': 'Polycarp'})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

    def test_name_is_unique(self):
        """ test artist name on the form is unique """
        form = ArtistForm({'name': 'georges_braque',
                          'friendly_name': 'Georges Braque'})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
