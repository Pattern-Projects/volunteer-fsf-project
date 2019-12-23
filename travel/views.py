from django.shortcuts import render

# Create your views here.
def get_travel_post(request):
    """
        Retrieve travel page content and show here
    """
    return render(request, "travel_post.html")