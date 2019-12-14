from django.shortcuts import render
from .models import Post
# Create your views here.
def get_travel_posts(request):
    """
        Retrieve all travel posts and show here
    """
    posts = Post.objects.all().order_by('-published_date')
    return render(request, "posts.html", {'posts': posts})
