from django.test import TestCase
from volunteer.views import get_camps, create_camp, edit_camp
from volunteer.models import Camp

# volunteer View Tests
class modelTestCase(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camps.html")
    
    def test_get_add_camp_page(self):
        page = self.client.get("/add_camp")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camp_form.html")
    
    def test_get_edit_camp_page(self):
        camp = Camp(name="Georgia")
        camp.save()
        page = self.client.get("/edit_camp/{0}".format(camp.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camp_form.html")
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit_camp/1")
        self.assertEqual(page.status_code, 404)