from django.conf.urls import url
from .views import get_travel_posts

urlpatterns = [
    url(r'^$', get_travel_posts, name='get_travel_posts'),
]