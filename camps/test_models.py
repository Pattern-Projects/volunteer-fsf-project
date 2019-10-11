from django.test import TestCase
from .models import Camp
from django.utils import timezone

class TestCampModels(TestCase):
    """
    Test Case - Camp Model
    """

    def test_camp_exists(self):
        camp = Camp(title="Camp")
        self.assertTrue(camp)

    def test_camp_information_values(self):
        camp = Camp(
            title="Camp",
            country = "Ireland",
            organisation = "Volunteer-Ireland",
            description = "A camp in Ireland"
            )

        self.assertEqual("Camp", camp.title)
        self.assertEqual("Ireland", camp.country)
        self.assertEqual("Volunteer-Ireland", camp.organisation)
        self.assertEqual("A camp in Ireland", camp.description)

    def test_camp_details_values(self):
        camp = Camp(
            positions=6,
            positions_female = 3,
            positions_male = 3,
            start_date = timezone.now,
            end_date = timezone.now,
            extra_host_country_fee = 250.50,
            extra_host_country_fee_currency = "Euro"
            )

        self.assertEqual(6, camp.positions)
        self.assertEqual(3, camp.positions_female)
        self.assertEqual(3, camp.positions_male)
        self.assertTrue(camp.start_date)
        self.assertTrue(camp.end_date)
        self.assertEqual(250.50, camp.extra_host_country_fee)
        self.assertEqual("Euro", camp.extra_host_country_fee_currency)


    def test_camp_information_values(self):
        camp = Camp(
            created_date = timezone.now,
            published_date = timezone.now,
            tag="Irish camp")

        self.assertTrue(camp.created_date)
        self.assertTrue(camp.published_date)
        self.assertEqual("Irish camp", camp.tag)

    def test_camp_as_a_string(self):
        camp = Camp(title="A camp")
        self.assertEqual("A camp", str(camp))