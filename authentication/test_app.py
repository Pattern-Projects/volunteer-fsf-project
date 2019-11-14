from django.apps import apps
from django.test import TestCase
from .apps import AuthenticationConfig


class TestAuthenticationConfig(TestCase):

    def test_app(self):
        self.assertEqual("authentication", AuthenticationConfig.name)
        self.assertEqual("authentication", apps.get_app_config("authentication").name)