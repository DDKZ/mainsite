from django.shortcuts import render, redirect
from aspc.auth2.views import guest_login
from django.core.urlresolvers import reverse
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.user.is_anonymous():
        return guest_login(request,next_page=reverse('geonet_home'))
    else:
        return HttpResponse("hello world")