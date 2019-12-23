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
import authentication.urls as urls_authentication
import blog.urls as urls_blog
import camps.urls as urls_camps
import cart.urls as urls_cart
import checkout.urls as urls_checkout
import search.urls as urls_search
import travel.urls as urls_travel

urlpatterns = [
    url(r'^admin', admin.site.urls),

    url(r'^$', get_camps, name="home"),
    url(r'^authentication/', include(urls_authentication)),
    url(r'^blog/', include(urls_blog)),
    url(r'^camps/', include(urls_camps)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^travel/', include(urls_travel), name="travel"),

    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
handler400=error404
