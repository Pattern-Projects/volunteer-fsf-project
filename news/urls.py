from django.conf.urls import url
from .views import get_posts, post_details, create_or_edit_a_post

urlpatterns = [
    url(r'^$', get_posts, name='news'),
    url(r'^(?P<pk>\d+)$', post_details, name='post_details'),
    url(r'new_post/$', create_or_edit_a_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit_post$', create_or_edit_a_post, name='edit_post'),
    url(r'new_news/$', create_or_edit_a_post, name='new_news'),

]