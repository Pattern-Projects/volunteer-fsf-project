from django.shortcuts import render

# Create your views here.
def get_goals_post(request):
    """
        Retrieve goals page content and show here
    """
    return render(request, "goals_post.html")