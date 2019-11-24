from django.conf.urls import url
from .views import search_camps

urlpatterns = [
    url(r'^$', search_camps, name='search_camps'),
]