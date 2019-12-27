from django.apps import apps
from django.test import TestCase
from .apps import DonateConfig


class TestDonateConfig(TestCase):

    def test_app(self):
        self.assertEqual("donate", DonateConfig.name)
        self.assertEqual("donate", apps.get_app_config("donate").name)