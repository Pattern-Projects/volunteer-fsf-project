from django.test import TestCase
from django.shortcuts import get_object_or_404

class TestTravelViews(TestCase):

    def test_get_travel_post(self):
        """
        Test that travel_posts returns 
        and renders the "travel_post.html" template
        """
        page = self.client.get("/travel/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "travel_post.html")