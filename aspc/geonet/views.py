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

def requestFriend(request, user_id):
    if request.user.is_anonymous():
        return HttpResponse("failure")
    other_user = User.objects.get(user_id)
    createGeoUser(other_user)
    other_geouser = other_user.geouser
    other_geouser.requests.add(request.user.geouser)
    return HttpResponse("success")

def approveFriend(request, user_id):
    if request.user.is_anonymous():
        return HttpResponse("failure")
    other_user = User.objects.get(user_id)
    createGeoUser(other_user)
    geouser = request.user.geouser
    approved_geouser = other_user.geouser
    if approved_geouser in geouser.requests:
        geouser.requests.remove(approved_geouser)
        geouser.friends.add(approved_geouser)
        approved_geouser.friends.add(geouser)
        return HttpResponse("success")
    else:
        return HttpResponse("failure")

def selfUpdate(request):
    if request.user.is_anonymous():
        return HttpResponse("failure")
    geouser = request.user.geouser
    long, lati = request.GET['long'], request.GET['lati']
    geouser.longitude = long
    geouser.latitude = lati
    return HttpResponse("success")

def createGeoUser(user):
    if len(GeoUser.objects.filter(user=user)) == 0:
        geouser = GeoUser(user=user)
        geouser.save()