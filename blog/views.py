from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import BlogPostForm

# Create your views here.
def get_travel_posts(request):
    """
        Retrieve all travel posts and show here
    """
    posts = Post.objects.all().order_by('-published_date')
    return render(request, "posts.html", {'posts': posts})

def post_details(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it tot hte 'postdetauils.html' template.
    Or return a 404 if the post is not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "post.html", {'post': post})

def create_or_edit_a_post(request, pk=None):
    """
    A view that is used to create
    or edit a post depending on the Post ID
    And rendering it to the 'edit_post.html' template
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})