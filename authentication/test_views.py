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

    def test_register_user(self):
        """
        Test that a user is registered
        """
        page = self.client.post("/authentication/registration", {'email': 'camp@mail.com', 'username': 'JohnnyO', 'password1' : 'Westqu3st', 'password2': 'Westqu3st'})
        self.assertEqual(page.status_code, 302)
        
    def test_open_profile(self):
        """
        Test that a user can visit the profile page
        only of logged in
        """
        # Visit profile before register
        page = self.client.get("/authentication/profile")
        self.assertEqual(page.status_code, 302)
        # Register user
        page = self.client.post("/authentication/registration", {'email': 'camp@mail.com', 'username': 'JohnnyO', 'password1' : 'Westqu3st', 'password2': 'Westqu3st'})
        self.assertEqual(page.status_code, 302)
        # Visit profile after register
        page = self.client.get("/authentication/profile")
        self.assertEqual(page.status_code, 200)
        
    def test_login_user(self):
        """
        Test that a user is registered
        """
        # Register
        page = self.client.post("/authentication/registration", {'email': 'camp@mail.com', 'username': 'JohnnyO', 'password1' : 'Westqu3st', 'password2': 'Westqu3st'})
        self.assertEqual(page.status_code, 302)
        # Logout
        page = self.client.get("/authentication/logout")
        self.assertEqual(page.status_code, 302)
        # Log In
        page = self.client.post("/authentication/login", {'username': 'JohnnyO', 'password' : 'Westqu3st'})
        self.assertEqual(page.status_code, 200)
        
    def test_already_authenticated_login(self):
        """
        Test that a user that is already logged in
        is redirected to profile if trying to login
        """
        # Register
        page = self.client.post("/authentication/registration", {'email': 'camp@mail.com', 'username': 'JohnnyO', 'password1' : 'Westqu3st', 'password2': 'Westqu3st'})
        self.assertEqual(page.status_code, 302)
        # Login
        page = self.client.get("/authentication/login")
        self.assertEqual(page.status_code, 302)

    def test_already_authenticated_registration(self):
        """
        Test that a user that is already logged in
        is redirected to profile if trying to register
        """
        # Register
        page = self.client.post("/authentication/registration", {'email': 'camp@mail.com', 'username': 'JohnnyO', 'password1' : 'Westqu3st', 'password2': 'Westqu3st'})
        self.assertEqual(page.status_code, 302)
        # Login
        page = self.client.get("/authentication/registration")
        self.assertEqual(page.status_code, 302)

