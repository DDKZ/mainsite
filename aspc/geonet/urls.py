from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from aspc.geonet.views import home, requestFriend, approveFriend

urlpatterns = [
    url(r'^$', home, name="geonet_home"),
    url(r'^request/(?P<geouser_id>[0-9]+)/$', requestFriend, name='friend_request'),
    url(r'^approve/(?P<geouser_id>[0-9]+)/$', approveFriend, name='friend_approve')
]
