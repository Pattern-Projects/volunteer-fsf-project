from django.test import TestCase
from django.shortcuts import get_object_or_404

class TestTravelViews(TestCase):

    def test_get_goals_post(self):
        """
        Test that goals_posts returns 
        and renders the "goals_post.html" template
        """
        page = self.client.get("/goals/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "goals_post.html")