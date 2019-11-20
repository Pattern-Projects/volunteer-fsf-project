from django.test import TestCase
from .forms import CampForm
from django.utils import timezone

# Create your tests here.
class TestCampForms(TestCase):

    def test_can_create_a_camp_with_minimum_details(self):
        form = CampForm({'title': 'A camp', 'region' : 'West', 'country': 'Ireland', 'continent' : 'EUROPE', 'organisation': 'Volunteer-Ireland', 'description': 'A camp','positions' : 0, 'positions_male' : 0, 'positions_female' : 0, 'positions_other' : 0, 
        'start_date': '2019-11-15','end_date': '2019-11-15','created_date': timezone.now(),'published_date': timezone.now()
        })
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_data(self):
        form = CampForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])


