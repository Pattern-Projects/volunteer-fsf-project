from django.conf.urls import url
from .views import get_camps, camp_details, create_or_edit_a_volunteer_camp, archive_camp, delete_camp

urlpatterns = [
    url(r'^$', get_camps, name='get_camps'),
    url(r'^(?P<pk>\d+)/$', camp_details, name='camp_details'),
    url(r'new_camp/$', create_or_edit_a_volunteer_camp, name='new_camp'),
    url(r'^(?P<pk>\d+)/edit_camp/$', create_or_edit_a_volunteer_camp, name='edit_camp'),
    url(r'^(?P<pk>\d+)/archive_camp/$', archive_camp, name='archive_camp'),
    url(r'^(?P<pk>\d+)/delete_camp/$', delete_camp, name='delete_camp'),
    
]
