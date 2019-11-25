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
        camp = Camp(title="Camp", price=100)
        camp.save()

        page = self.client.get("/camps/{0}/".format(camp.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camp.html")


    def test_camp_details_of_uknown_camp(self):
        """
        Test that a 404 is returned if the camp id
        does not match an existing camp
        """
        camp = Camp(title="Camp", price=100)
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

    def test_camp_is_created(self):
        """
        Test that a test is created by post method
        """
        page = self.client.post("/camps/new_camp/", {'title': 'A Camp', 'tagline': 'Here now', 'region' : 'West', 'country': 'Ireland', 'continent' : 'EUROPE', 'organisation': 'Volunteer-Ireland', 'positions' : 0, 'positions_male' : 0, 'positions_female' : 0, 'positions_other' : 0, 
        'description': 'A camp', 'start_date': '2019-11-15','end_date': '2019-11-15', 'price': '100', 'created_date': '2019-11-15 07:04:08','published_date': '2019-11-15 07:04:08'
        })
        camp = get_object_or_404(Camp, pk=1)
        self.assertEqual("A Camp", camp.title)
        self.assertEqual("Ireland", camp.country)
        self.assertEqual("Volunteer-Ireland", camp.organisation)
        self.assertEqual("A camp", camp.description)
        self.assertRedirects(page, "/camps/", status_code=302, target_status_code=200)

    def test_edit_camp_page(self):
        """
        Test that the edit_camp page opens
        when visited
        """
        camp = Camp(title="Camp", price=100)
        camp.save()
        page = self.client.get("/camps/{0}/edit_camp/".format(camp.id))

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_camp.html")

    def test_camp_is_edited(self):
        """
        Test that a camp can have details edited through
        the edit_camp.html page
        """
        camp = Camp(title= 'This camp', region="West", country='Ireland', continent="EUROPE", organisation= 'Volunteer-Ireland', description= 'A camp',
        start_date= '2019-11-15',end_date= '2019-11-15', price= 100, created_date= '2019-11-15 07:04:08',published_date='2019-11-15 07:04:08'
        )
        camp.save()
        page = self.client.post("/camps/{0}/edit_camp/".format(camp.id), {'title': 'New Camp', 'region' : 'West', 'country': 'Ireland', 'continent' : 'EUROPE', 'organisation': 'Volunteer-Ireland', 'positions' : 0, 'positions_male' : 0, 'positions_female' : 0, 'positions_other' : 0, 
        'description': 'A camp', 'start_date': '2019-11-15','end_date': '2019-11-15', 'price': '100', 'created_date': '2019-11-15 07:04:08','published_date': '2019-11-15 07:04:08'
        })
        camp = get_object_or_404(Camp, pk=camp.id)
        self.assertRedirects(page, "/camps/", status_code=302, target_status_code=200)
        self.assertEqual("New Camp", camp.title)

    def test_camp_is_archived(self):
        """
        Test that a test is not archved when created
        then archived after archive_camp() is called with id
        """
        camp = Camp(title="Camp", price=100)
        camp.save()
        camp = get_object_or_404(Camp, pk=1)
        self.assertFalse(camp.archived)
        
        page = self.client.get("/camps/{0}/archive_camp/".format(camp.id))
        camp = get_object_or_404(Camp, pk=camp.id)
        self.assertTrue(camp.archived)
        
    def test_camp_is_deleted(self):
        """
        Test that a camp is created
        then deleted after delete_camp() is called with id
        """
        # Create a camp, test it is added to db
        camp = Camp(title="Camp", price=100)
        camp.save()
        results = Camp.objects.all()
        self.assertEqual(1, results.count())
        
        # Delete camp, test it is removed from db
        camp = get_object_or_404(Camp, pk=1)
        page = self.client.get("/camps/{0}/delete_camp/".format(camp.id))
        self.assertEqual(0, results.count())
        