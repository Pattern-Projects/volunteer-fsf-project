"""
volunteer_fsf_project URL Configuration
"""
from django.conf.urls import url, include, handler400, handler500
from django.contrib import admin
from django.views import static
from .settings import MEDIA_ROOT

from .views import error404, error500
from authentication.views import login, registration, logout
from travel.views import get_travel_post
import authentication.urls as urls_authentication
import stories.urls as urls_stories
import camps.urls as urls_camps
import cart.urls as urls_cart
import checkout.urls as urls_checkout
import news.urls as urls_news
import privacy.urls as urls_privacy
import search.urls as urls_search
import travel.urls as urls_travel

urlpatterns = [
    url(r'^admin', admin.site.urls),

    url(r'^$', get_travel_post, name="home"),
    url(r'^authentication/', include(urls_authentication)),
    url(r'^stories/', include(urls_stories), name="stories"),
    url(r'^camps/', include(urls_camps), name="camps"),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^news/', include(urls_news), name="news"),
    url(r'^privacy/', include(urls_privacy), name="privacy"),
    url(r'^search/', include(urls_search)),
    url(r'^travel/', include(urls_travel), name="travel"),

    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
handler400=error404
