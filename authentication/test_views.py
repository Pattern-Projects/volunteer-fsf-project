from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib import messages

# volunteer View Tests
class modelTestCase(TestCase):

    def test_auth_logout(self):
        page = self.client.get("/authentication/logout")
        self.assertEqual(page.status_code, 302)
        self.assertTrue(messages.success)

    def test_login_page(self):
        page = self.client.get("/authentication/login")
        self.assertEqual(page.status_code, 200)

    def test_registration_page(self):
        page = self.client.get("/authentication/registration")
        self.assertEqual(page.status_code, 200)
