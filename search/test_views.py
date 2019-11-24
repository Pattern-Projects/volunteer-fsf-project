from django.test import TestCase
from django.shortcuts import get_object_or_404
from camps.models import Camp

class TestSearchViews(TestCase):

    def test_query_in_camp_title(self):
        """
        Test that the search query 
        is present in the camp title.
        Creates 3 camps, one with title Find
        Searches for Find, then counts number of results
        """
        camp = Camp(title="Camp")
        camp.save()
        camp = Camp(title="Find")
        camp.save()
        camp = Camp(title="Camp")
        camp.save()

        page = self.client.get("/search/?query=Find")
        camps = page.context['camps']
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camps.html")
        self.assertEqual(1, camps.count())


    def test_query_in_camp_region(self):
        """
        Test that the search query 
        is present in the camp region.
        Creates 3 camps, one with region Find
        Searches for Find, then counts number of results
        """
        camp = Camp(title="Camp", region="Region")
        camp.save()
        camp = Camp(title="Camp", region="Find")
        camp.save()
        camp = Camp(title="Camp", region="Region")
        camp.save()

        page = self.client.get("/search/?query=Find")
        camps = page.context['camps']
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camps.html")
        self.assertEqual(1, camps.count())

    def test_query_in_camp_country(self):
        """
        Test that the search query 
        is present in the camp country.
        Creates 3 camps, one with country Find
        Searches for Find, then counts number of results
        """
        camp = Camp(title="Camp", country="Country")
        camp.save()
        camp = Camp(title="Camp", country="Find")
        camp.save()
        camp = Camp(title="Camp", country="Country")
        camp.save()

        page = self.client.get("/search/?query=Find")
        camps = page.context['camps']
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camps.html")
        self.assertEqual(1, camps.count())

    def test_query_in_camp_continent(self):
        """
        Test that the search query 
        is present in the camp continent.
        Creates 3 camps, one with continent Find
        Searches for Find, then counts number of results
        """
        camp = Camp(title="Camp", continent="Continent")
        camp.save()
        camp = Camp(title="Camp", continent="Find")
        camp.save()
        camp = Camp(title="Camp", continent="Continent")
        camp.save()

        page = self.client.get("/search/?query=Find")
        camps = page.context['camps']
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "camps.html")
        self.assertEqual(1, camps.count())









        

        