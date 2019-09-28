from django.apps import apps
from django.test import TestCase
from .apps import VolunteerConfig


class TestTodoConfig(TestCase):

    def test_app(self):
        self.assertEqual("volunteer", VolunteerConfig.name)
        self.assertEqual("volunteer", apps.get_app_config("volunteer").name)