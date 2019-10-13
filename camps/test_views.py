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

    def xtest_camp_details(self):
        """
        Test that camp_details creates a Camp object and
        render it with the 'camp.html' template.
        Or return a 404 if the camp is not found
        """
        camp = Camp(
            title="Camp",
            country = "Ireland",
            organisation = "Volunteer-Ireland",
            description = "A camp in Ireland"
            )
        camp.save()

        page = self.client.get("/{0}".format(camp.id))
        self.assertEqual(page.status_code, 404)
        self.assertTemplateUsed(page, "camp.html")

    def xtest_create_or_edit_a_volunteer_camp(self):
        """
        test that a volunteer camp is opened with the 'edit_camp.html' template
        """
        camp = Camp(
            title="Camp",
            country = "Ireland",
            organisation = "Volunteer-Ireland",
            description = "A camp in Ireland"
            )
        camp.save()

        page = self.client.get("/{0}/edit_camp".format(camp.id))
        self.assertEqual(page.status_code, 404)
        self.assertTemplateUsed(page, "edit_camp.html")