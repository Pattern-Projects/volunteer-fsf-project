from django.conf.urls import url
from .views import get_camps, camp_details, filter_by_continent, create_or_edit_a_volunteer_camp, archive_camp, get_archived_camps, delete_camp

urlpatterns = [
    url(r'^$', get_camps, name='camps'),
    url(r'^$', get_camps, name='get_camps'),
    url(r'^(?P<pk>\d+)$', camp_details, name='camp_details'),
    url(r'^filter_by_continent/(?P<continent>\w+)', filter_by_continent, name='filter_by_continent'),
    url(r'new_camp/$', create_or_edit_a_volunteer_camp, name='new_camp'),
    url(r'^(?P<pk>\d+)/edit_camp$', create_or_edit_a_volunteer_camp, name='edit_camp'),
    url(r'^(?P<pk>\d+)/archive_camp$', archive_camp, name='archive_camp'),
    url(r'^archived_camps$', get_archived_camps, name='get_archived_camps'),
    url(r'^(?P<pk>\d+)/delete_camp$', delete_camp, name='delete_camp'),
    
]
