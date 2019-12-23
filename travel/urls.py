from django.conf.urls import url
from .views import get_travel_post

urlpatterns = [
    url(r'^$', get_travel_post, name='travel'),
]