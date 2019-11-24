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

        def test_registration_success(self):
            form = UserRegistrationForm({'email': 'email@mail.com', 'username':"John", 'password1':'adsjNSID34', 'password2':'adsjNSID34'})
            self.assertTrue(form.is_valid())
            
        def test_registration_missing_name(self):
            form = UserRegistrationForm({'email': 'email@mail.com', 'username':"", 'password1':'adsjNSID34', 'password2':'adsjNSID34'})
            self.assertEqual(form.errors['username'], [u'This field is required.'])

        def test_registration_bad_email(self):
            form = UserRegistrationForm({'email': 'email', 'username':"John", 'password1':'adsjNSID34', 'password2':'adsjNSID34'})
            self.assertEqual(form.errors['email'], [u'Enter a valid email address.'])
