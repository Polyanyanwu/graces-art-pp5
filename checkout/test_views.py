""" Test Checkout views """
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import AnonymousUser

from .views import request_cancel_order


class TestViews(TestCase):
    """ test views """

    fixtures = ["test_fixture/system_preference.json",
                "test_fixture/home_message.json"]

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        """ test that home page responds """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_anonymous_user_cannot_cancel_order(self):
        """ Anonymous user cannot cancel order
           user is redirected to login page"""
        request = self.factory.post('/cancel_order')
        request.user = AnonymousUser()
        response = request_cancel_order(request)
        assert response.status_code == 302
        response.client = Client()
        self.assertRedirects(response, '/accounts/login/?next=/cancel_order',
                             status_code=302, target_status_code=200)
