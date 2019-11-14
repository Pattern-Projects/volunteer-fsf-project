from django.test import TestCase
# from authentication.models import Camp
from .forms import UserLoginForm, UserRegistrationForm

# authentication Form Tests
class modelTestCase(TestCase):
        def test_login_success(self):
            form = UserLoginForm({'username':"John", 'password':'password'})
            self.assertTrue(form.is_valid())
            
        def test_login_missing_name(self):
            form = UserLoginForm({'username':'', 'password':'password'})
            self.assertEqual(form.errors['username'], [u'This field is required.'])