from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Camp

class TestCampViews(TestCase):

    def test_get_camps(self):
        """
        Test that get_camps returns a list of camps
        and renders them to the "camps.html" template
        """
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camps.html")

    def test_camp_details(self):
        """
        Test that camp_details creates a Camp object and
        render it with the 'camp.html' template.
        Or return a 404 if the camp is not found
        """
        camp = Camp(
            title="Camp"
            )
        camp.save()

        page = self.client.get("/camps/{0}/".format(camp.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camp.html")

        page = self.client.get("/camps/{0}/".format(2))
        self.assertEqual(page.status_code, 404)


    def test_create_or_edit_a_volunteer_camp(self):
        """
        test that a volunteer camp is opened with the 'edit_camp.html' template
        and that /new_camp redirects to /camps/new_camp/
        """
        page = self.client.get("/camps/new_camp/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_camp.html")

        page = self.client.get("/new_camp")
        self.assertRedirects(page, "/camps/new_camp/", status_code=302, target_status_code=200)
        # self.assertTemplateUsed(page, "edit_camp.html")
