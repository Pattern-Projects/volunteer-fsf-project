from django.conf.urls import url
from .views import get_goals_post

urlpatterns = [
    url(r'^$', get_goals_post, name='goals'),
]