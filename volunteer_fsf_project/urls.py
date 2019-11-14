"""volunteer_fsf_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from .settings import MEDIA_ROOT

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
