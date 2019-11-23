from django.conf.urls import url
from .views import profile, login, logout, registration

urlpatterns = [

    url(r'^$', profile, name="profile"),
    url(r'^profile$', profile, name="profile"),
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^registration$', registration, name="registration"),

]