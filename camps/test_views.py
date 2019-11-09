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
        """
        camp = Camp(title="Camp")
        camp.save()

        page = self.client.get("/camps/{0}/".format(camp.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camp.html")


    def test_camp_details_of_uknown_camp(self):
        """
        Test that a 404 is returned if the camp id
        does not match an existing camp
        """
        camp = Camp(title="Camp")
        camp.save()

        page = self.client.get("/camps/{0}/".format(2))
        self.assertEqual(page.status_code, 404)


    def test_create_or_edit_a_volunteer_camp(self):
        """
        test that a volunteer camp is opened with the
        'edit_camp.html' template
        """
        page = self.client.get("/camps/new_camp/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_camp.html")


    def test_for_redirect(self):
        """
        Test that browser redirects from '/new_camp'
        to '/camps/new_camp/
        """

        page = self.client.get("/new_camp")
        self.assertRedirects(page, "/camps/new_camp/", status_code=302, target_status_code=200)

    def test_camp_is_created(self):
        """
        Test that a test is created by post method
        """
        page = self.client.post("/camps/new_camp/", {"title": "New Camp", "country": "Ireland", "organisation": "VI", "description": "A camp"})
        camp = get_object_or_404(Camp, pk=1)
        self.assertEqual("New Camp", camp.title)
        self.assertEqual("Ireland", camp.country)
        self.assertEqual("VI", camp.organisation)
        self.assertEqual("A camp", camp.description)

    def test_edit_camp_page(self):
        """
        Test that the edit_camp page opens
        when visited
        """
        camp = Camp(title="Camp")
        camp.save()
        page = self.client.get("/camps/{0}/edit_camp/".format(camp.id))

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_camp.html")

    def test_camp_is_edited(self):
        """
        Test that a camp can have details edited through
        the edit_camp.html page
        """
        camp = Camp(title="A camp")
        camp.save()
        page = self.client.post("/camps/{0}/edit_camp/".format(camp.id), {"title": "New Camp", "country": "Ireland", "organisation": "VI", "description": "A camp"})
        self.assertRedirects(page, "/camps/", status_code=302, target_status_code=200)
        # self.assertEqual("New Camp", camp.title)
