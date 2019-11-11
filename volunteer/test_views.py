from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib import messages
from volunteer.views import get_camps, create_camp, edit_camp
from volunteer.models import Camp


# volunteer View Tests
class modelTestCase(TestCase):

    def test_auth_logout(self):
        page = self.client.get("/logout")
        self.assertEqual(page.status_code, 302)
        self.assertTrue(messages.success)

    def xtest_login_page(self):
        page = self.client.get("/login")
        self.assertEqual(page.status_code, 200)

    def xtest_registration_page(self):
        page = self.client.get("/registration")
        self.assertEqual(page.status_code, 200)

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camps.html")

    def xtest_get_add_camp_page(self):
        page = self.client.get("/new_camp")
        self.assertEqual(page.status_code, 302)
        self.assertTemplateUsed(page, "camp_form.html")

    def xtest_get_edit_camp_page(self):
        camp = Camp(name="Camp")
        camp.save()

        page = self.client.get("/{0}/edit_camp/".format(camp.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camp_form.html")

    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit_camp/1")
        self.assertEqual(page.status_code, 404)

    def xtest_post_create_camp(self):
        response = self.client.post("/add_camp", {'name': 'Camp', 'available': True})
        camp = get_object_or_404(Camp, pk=1)
        self.assertTrue(camp.available)

    def xtest_post_edit_a_camp(self):
        camp = Camp(name='Camp')
        camp.save()
        id = camp.id

        response = self.client.post("/edit_camp/{0}".format(id), {"name": "Second Camp", "available": True})
        camp = get_object_or_404(Camp, pk=id)

        self.assertEqual("Second Camp", camp.name)
        self.assertTrue(camp.available)
