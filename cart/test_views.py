from django.test import TestCase
from .views import add_to_cart, adjust_cart

class TestCampViews(TestCase):
    def test_view_cart(self):
        """
        Test that the cart page is opened
        """
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")


    def test_add_to_cart_successful(self):
        """
        Test that a camp is added to cart
        """
        page = self.client.post("/cart/add/0", {'quantity': '1'})
        self.assertEqual(page.status_code, 302)
        page = self.client.post("/cart/add/0", {'quantity': '1'})
        self.assertEqual(page.status_code, 302)


    def test_adjust_cart_successful(self):
        """
        Test that a cart is adjusted
        """
        page = self.client.post("/cart/add/0", {'quantity': '1'})
        self.assertEqual(page.status_code, 302)
        page = self.client.post("/cart/adjust/0", {'quantity': '1'})
        self.assertEqual(page.status_code, 302)
        