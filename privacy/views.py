from django.shortcuts import render

# Create your views here.
def get_privacy_post(request):
    """
        Retrieve privacy page content and show here
    """
    return render(request, "privacy_post.html")