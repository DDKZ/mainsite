from django.shortcuts import render, redirect, get_object_or_404
from aspc.auth2.views import guest_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from aspc.geonet.models import GeoUser
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.user.is_anonymous():
        return guest_login(request,next_page=reverse(home))
    createGeoUser(request.user)
    return render(request,'geonet/landing.html')

def createGeoUser(user):
    if len(GeoUser.objects.filter(user=user)) == 0:
        geouser = GeoUser(user=user)
        geouser.save()