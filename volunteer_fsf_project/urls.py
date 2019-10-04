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
from django.conf.urls import url
from django.contrib import admin
from volunteer.views import login, registration, logout, get_camps, create_camp, edit_camp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_camps, name="home"),
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^registration$', registration, name="registration"),
    url(r'^get_camps$', get_camps, name="get_camps"),
    url(r'^add_camp$', create_camp),
    url(r'^edit_camp/(?P<id>\d+)$', edit_camp)
]
