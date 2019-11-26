from django.test import TestCase
from django.contrib import messages 
from camps.models import Camp
from cart.views import add_to_cart, adjust_cart
from .forms import MakePaymentForm, OrderForm

class TestCheckoutConfig(TestCase):

    def test_checkout_rendered(self):
        """
        Test that a checkout page is opened
        """
        # Register User
        page = self.client.post("/authentication/registration", {'email': 'camp@mail.com', 'username': 'JohnnyO', 'password1' : 'Westqu3st', 'password2': 'Westqu3st'})
        self.assertEqual(page.status_code, 302)
        # Visit checkout
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")

    def test_checkout_unsuccessful(self):
        """
        Test that a checkout page post of wrong details
        returns error message
        """
        # Register User
        page = self.client.post("/authentication/registration", {'email': 'camp@mail.com', 'username': 'JohnnyO', 'password1' : 'Westqu3st', 'password2': 'Westqu3st'})
        self.assertEqual(page.status_code, 302)
        # Make camp
        camp = Camp(title="Camp", price=100)
        camp.save()
        # Add camp to cart
        page = self.client.post("/cart/add/{0}/".format(camp.id), {'quantity': '1'})
        # Post checkout
        page = self.client.post("/checkout/", 
            {
            'full_name' : 'John',
            'phone_number' : '0854561235',
            'country' : 'Ireland',
            'postcode' : '0000',
            'town_or_city' : 'Town',
            'street_address1' : 'Fake Street',
            'street_address2' : 'Baker Street',
            'county' : 'Yes',
            'date' : '2019-11-15',
            }
        )
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
        

    def xtest_checkout_successful(self):
        """
        Test that a checkout post of 
        correct details results in
        a successful checkout
        """
        # Register User
        page = self.client.post("/authentication/registration", {'email': 'camp@mail.com', 'username': 'JohnnyO', 'password1' : 'Westqu3st', 'password2': 'Westqu3st'})
        self.assertEqual(page.status_code, 302)
        # Make camp
        camp = Camp(title="Camp", price=100)
        camp.save()
        # Add camp to cart
        page = self.client.post("/cart/add/{0}/".format(camp.id), {'quantity': '1'})
        # Post checkout
        page = self.client.post("/checkout/", 
            {
            'full_name' : 'John',
            'phone_number' : '0854561235',
            'country' : 'Ireland',
            'postcode' : '0000',
            'town_or_city' : 'Town',
            'street_address1' : 'Fake Street',
            'street_address2' : 'Baker Street',
            'county' : 'Yes',
            'date' : '2019-11-15',

            'credit_card_number' : '4242424242424242',
            'cvv' : '111',
            'expiry_month' : '1',
            'expiry_year' : '2020',
            #Issue here: creating a stripe id_token, how?
            'stripe_id' : '1',
            }
        )


    