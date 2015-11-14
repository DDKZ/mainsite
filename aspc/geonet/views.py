from django.shortcuts import render, redirect, get_object_or_404
from aspc.auth2.views import guest_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from aspc.geonet.models import GeoUser
# Create your views here.

def home(request):
    if request.user.is_anonymous():
        return guest_login(request,next_page=reverse(home))
    return render(request,'geonet/landing.html')

def requestFriend(request, geouser_id):
    if request.user.is_anonymous():
        return HttpResponse("failure")
    other_geouser = get_object_or_404(GeoUser, geouser_id)
    other_geouser.requests.add(request.user.geouser)
    return HttpResponse("success")

def approveFriend(request, geouser_id):
    if request.user.is_anonymous():
        return HttpResponse("failure")
    geouser = request.user.geouser
    approved_geouser = get_object_or_404(GeoUser, geouser_id)
    if approved_geouser in geouser.requests:
        geouser.friends.add(approved_geouser)
        approved_geouser.friends.add(geouser)
        return HttpResponse("success")
    else:
        return HttpResponse("failure")


