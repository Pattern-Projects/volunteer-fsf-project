from django.test import TestCase
from volunteer.models import Camp
from volunteer.forms import CampForm

# volunteer Model Tests
class modelTestCase(TestCase):
    def setUp(self):
        # reusable variables
        newCamp = Camp()
        
    def test_correct_message_for_missing_name(self):
        form = CampForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        
    def test_camp_as_a_string(self):
        camp = Camp(name="Camp")
        self.assertEqual("Camp", str(camp))
