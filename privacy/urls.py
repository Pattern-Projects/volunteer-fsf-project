from django.conf.urls import url
from .views import get_privacy_post

urlpatterns = [
    url(r'^$', get_privacy_post, name='privacy'),
]