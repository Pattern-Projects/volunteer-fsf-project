from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Camp

class TestCampViews(TestCase):

    def test_get_camps(self):
        """
        Test that get_camps returns a list of camps
        and renders them to the "camps.html" template
        """

    def test_camp_details(request, pk):
    """
    Test that camp_details creates a Camp object and
    render it with the 'camp.html' template.
    Or return a 404 if the camp is not found
    """

def test_create_or_edit_a_volunteer_camp(request, pk=None):
    """
    test that a volunteer camp is opened with the 'edit_camp.html' template
    """
