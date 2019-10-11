from django.conf.urls import url
from .views import get_camps, camp_details, create_or_edit_a_volunteer_camp

urlpatterns = [
    url(r'^$', get_camps, name='get_camps'),
]