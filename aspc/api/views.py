from itertools import chain
from django.contrib.auth.models import User
from django.shortcuts import render
from aspc.geonet.models import GeoUser, GeoUserSerializer
from aspc.menu.models import Menu, MenuSerializer
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.authtoken.models import Token
from django.views.decorators.cache import never_cache

@never_cache
def api_home(request):
    current_user = request.user
    token = None
    if current_user.is_active:
        token = Token.objects.get_or_create(user=current_user)[0].key
    return render(request, 'api/landing.html', {
        'token': token
    })

@never_cache
def api_token(request):
    current_user = request.user
    token = None
    if current_user.is_active:
        token = Token.objects.get_or_create(user=current_user)[0].key
    import json
    jsonToken = {'token': token}
    data = json.dumps(jsonToken)
    return HttpResponse(data, content_type='application/json')

class MenuList(APIView):
    """
    List all menus
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get(self, request, format=None):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

class MenuDiningHallDetail(APIView):
    """
    Retrieve a list of menus by their dining hall
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get_object(self, dining_hall):
        try:
            return Menu.objects.filter(dining_hall=dining_hall)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, dining_hall, format=None):
        menus = self.get_object(dining_hall)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

class MenuDayDetail(APIView):
    """
    Retrieve a list of menus by their day
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get_object(self, day):
        try:
            return Menu.objects.filter(day=day)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, day, format=None):
        menus = self.get_object(day)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

class MenuDiningHallDayDetail(APIView):
    """
    Retrieve a list of menus by their dining hall and day
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get_object(self, dining_hall, day):
        try:
            return Menu.objects.filter(dining_hall=dining_hall).filter(day=day)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, dining_hall, day, format=None):
        menus = self.get_object(dining_hall, day)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

class MenuDiningHallDayMealDetail(APIView):
    """
    Retrieve a menu by its dining hall, day, and meal
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get_object(self, dining_hall, day, meal):
        try:
            return Menu.objects.filter(dining_hall=dining_hall).filter(day=day).filter(meal=meal)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, dining_hall, day, meal, format=None):
        menus = self.get_object(dining_hall, day, meal)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

class GeolocationList(APIView):
    """
    List all geolocation list
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get(self, request, format=None):
        geousers = GeoUser.objects.all()
        serializer = GeoUserSerializer(geousers, many=True)
        return Response(serializer.data)

class MapMe(APIView):
    """
    Gets your current geolocation and allows you to post your geolocation
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get(self, request, format=None):
        me = GeoUser.objects.filter(user=request.user).first()
        serializer = GeoUserSerializer(me)
        return Response(serializer.data)

    def put(self, request, format=None):
        me = GeoUser.objects.filter(user=request.user).first()
        serializer = GeoUserSerializer(me, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MapFriends(APIView):
    """
    Gets the geolocation of your friends
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get(self, request, format=None):
        me = GeoUser.objects.filter(user=request.user).first()
        friends = me.friends.all()
        serializer = GeoUserSerializer(friends, many=True)
        return Response(serializer.data)

class MapRequestFriends(APIView):
    """
    Request friends
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get(self, request, pk, format=None):
        other_user = User.objects.get(pk=pk)
        if len(GeoUser.objects.filter(user=request.user)) == 0:
            GeoUser.objects.create(user=request.user).save()
        if len(GeoUser.objects.filter(user=other_user)) == 0:
            GeoUser.objects.create(user=other_user).save()
        other_geouser = other_user.geouser
        other_geouser.requests.add(request.user.geouser)
        other_geouser.save()
        return Response(status=status.HTTP_201_CREATED)

class MapAcceptFriends(APIView):
    """
    Accept friends
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    throttle_classes = (UserRateThrottle,)

    def get(self, request, pk, format=None):
        other_user = User.objects.get(pk=pk)
        if len(GeoUser.objects.filter(user=request.user)) == 0:
            GeoUser.objects.create(user=request.user).save()
        me = request.user.geouser
        friend = other_user.geouser
        if friend in me.requests.all():
            me.requests.remove(friend)
            me.friends.add(friend)
            friend.friends.add(me)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)