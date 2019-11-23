"""
volunteer_fsf_project URL Configuration
"""
from django.conf.urls import url, include, handler400, handler500
from django.contrib import admin
from django.views import static
from .settings import MEDIA_ROOT

from .views import error404, error500
from authentication.views import login, registration, logout
from camps.views import get_camps
import camps.urls as urls_camps
import authentication.urls as urls_authentication

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', get_camps, name="home"),
    url(r'^camps/', include(urls_camps)),
    url(r'^authentication/', include(urls_authentication)),

    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
handler400=error404
