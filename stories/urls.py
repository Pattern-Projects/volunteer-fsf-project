from django.conf.urls import url
from .views import get_story_posts, story_post_details, create_or_edit_a_story_post

urlpatterns = [
    url(r'^$', get_story_posts, name='stories'),
    url(r'^(?P<pk>\d+)$', story_post_details, name='story_post_details'),
    url(r'new_story/$', create_or_edit_a_story_post, name='new_story'),
    url(r'^(?P<pk>\d+)/edit_post$', create_or_edit_a_story_post, name='edit_story_post'),

]