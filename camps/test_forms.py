from django.test import TestCase
from .forms import CampForm

# Create your tests here.
class TestCampForms(TestCase):

    def test_can_create_a_camp_with_minimum_details(self):
        form = CampForm({'title': 'A camp', 'country': 'Ireland', 'organisation': 'Volunteer-Ireland', 'description': 'A camp'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_data(self):
        form = CampForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])