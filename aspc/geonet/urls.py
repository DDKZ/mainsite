from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from aspc.geonet.views import home

urlpatterns = [
    url(r'^$', home, name="geonet_home"),
    url(r'^$')
    ]
