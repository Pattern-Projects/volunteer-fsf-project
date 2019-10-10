from django.test import TestCase
from .models import Camp

class campModelTestCase(TestCase):
    """
    Test Case - Camp Model
    """

    def test_camp_exists(self):
        camp = Camp(title="Camp")
        self.assertTrue(camp)

    def test_camp_attribute_values(self):
        camp = Camp(title="Camp",
        country = "Ireland",
        organisation = "Volunteer-Ireland")
        self.assertEqual("Camp", camp.title)
        self.assertEqual("Ireland", camp.country)
        self.assertEqual("Volunteer-Ireland", camp.organisation)
