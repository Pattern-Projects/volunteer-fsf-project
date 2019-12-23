from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class TravelPost(models.Model):
    """
    A single travel post for the travel page content
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
