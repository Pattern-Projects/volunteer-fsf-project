from django.shortcuts import render

def get_camps(request):
    """
    Create a view that will return a list
    of Camps and render them to the 'camps.html' template
    """

def camp_details(request, pk):
    """
    Create a view that returns a single
    Camp object based on the camp ID (pk) and
    render it with the 'camp.html' template.
    Or return a 404 if the camp is not found
    """

def create_or_edit_a_volunteer_camp(request, pk=None):
    """
    Create a view that is used to create
    or edit a volunteer camp depending on the Post ID
    """