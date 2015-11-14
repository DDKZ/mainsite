from django.shortcuts import render, redirect, get_object_or_404
from aspc.auth2.views import guest_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from aspc.geonet.models import GeoUser, FriendForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.user.is_anonymous():
        return guest_login(request,next_page=reverse('geonet_home'))
    createGeoUser(request.user)
    friend_form = FriendForm()
    return render(request,'geonet/landing.html',{'friend_form':friend_form})

def requestFriend(request):
    if request.user.is_anonymous():
        return HttpResponse("failure")
    firstName, lastName = request.POST['first_name'], request.POST['last_name']
    other_user_list = User.objects.filter(first_name=firstName).filter(last_name=lastName)
    if len(other_user_list) > 0:
        other_user = other_user_list[0]
    else:
        friend_form = FriendForm()
        return render(request,'geonet/landing.html',{'friend_form':friend_form,'request_message':'cannot find'})
    createGeoUser(other_user)
    other_geouser = other_user.geouser
    other_geouser.requests.add(request.user.geouser)
    friend_form = FriendForm()
    return render(request,'geonet/landing.html',{'friend_form':friend_form,'request_message':'request sent'})

def approveFriend(request, user_id):
    if request.user.is_anonymous():
        return HttpResponse("failure")
    other_user = User.objects.get(user_id)
    createGeoUser(other_user)
    geouser = request.user.geouser
    approved_geouser = other_user.geouser
    if approved_geouser in geouser.requests and approved_geouser is not geouser:
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