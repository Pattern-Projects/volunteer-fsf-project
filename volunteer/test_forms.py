from django.test import TestCase
# from volunteer.models import Camp
from volunteer.forms import CampForm

# volunteer Form Tests
class modelTestCase(TestCase):
        def test_can_create_an_camp_with_just_a_name(self):
            form = CampForm({'name':"Switzerland"})
            self.assertTrue(form.is_valid())
            
        def test_correct_message_for_missing_name(self):
            form = CampForm({'name':''})
            self.assertEqual(form.errors['name'], [u'This field is required.'])