from django.shortcuts import render, get_object_or_404, redirect
from .models import StoryPost
from .forms import StoryPostForm

# Create your views here.
def get_story_posts(request):
    """
        Retrieve travel page content and show here
    """
    posts = StoryPost.objects.all().order_by('-published_date')
    return render(request, "story_posts.html", {'posts': posts})

def story_post_details(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it tot hte 'postdetauils.html' template.
    Or return a 404 if the post is not found
    """
    post = get_object_or_404(StoryPost, pk=pk)
    post.views += 1
    post.save()
    return render(request, "story_post.html", {'post': post})

def create_or_edit_a_story_post(request, pk=None):
    """
    A view that is used to create
    or edit a post depending on the Post ID
    And rendering it to the 'edit_post.html' template
    """
    post = get_object_or_404(StoryPost, pk=pk) if pk else None
    if request.method == "POST":
        form = StoryPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(story_post_details, post.pk)
    else:
        form = StoryPostForm(instance=post)
    return render(request, 'edit_story_post.html', {'form': form})