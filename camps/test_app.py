from django.apps import apps
from django.test import TestCase
from .apps import CampsConfig


class TestCampsConfig(TestCase):

    def test_app(self):
        self.assertEqual("camps", CampsConfig.name)
        self.assertEqual("camps", apps.get_app_config("camps").name)