from django.test import TestCase
from django.shortcuts import get_object_or_404

class TestPrivacyViews(TestCase):

    def test_get_privacy_post(self):
        """
        Test that privacy_posts returns 
        and renders the "privacy_post.html" template
        """
        page = self.client.get("/privacy/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "privacy_post.html")