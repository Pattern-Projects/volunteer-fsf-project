from django.shortcuts import render, redirect, reverse

# Create your views here.
def get_travel_posts(request):
    """
        Retrieve all travel posts and show here
    """
    return render(request, "posts.html")
