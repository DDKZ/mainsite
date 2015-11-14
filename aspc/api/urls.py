from django.conf.urls import patterns, url, include
from aspc.api import views
from aspc.api.views import MenuList, MenuDiningHallDetail, MenuDayDetail, MenuDiningHallDayDetail, MenuDiningHallDayMealDetail, \
    MapMe, MapFriends, MapRequestFriends, MapAcceptFriends

urlpatterns = [
    url(r'menu/dining_hall/(?P<dining_hall>[^/]+)/day/(?P<day>[^/]+)/meal/(?P<meal>[^/]+)/?$', MenuDiningHallDayMealDetail.as_view()),
    url(r'menu/dining_hall/(?P<dining_hall>[^/]+)/day/(?P<day>[^/]+)/?$', MenuDiningHallDayDetail.as_view()),
    url(r'menu/day/(?P<day>[^/]+)/?$', MenuDayDetail.as_view()),
    url(r'menu/dining_hall/(?P<dining_hall>[^/]+)/?$', MenuDiningHallDetail.as_view()),
    url(r'menu/?$', MenuList.as_view()),
    url(r'maps/friends/request/(?P<pk>[0-9]+)/?', MapRequestFriends.as_view()),
    url(r'maps/friends/accept/(?P<pk>[0-9]+)/?', MapAcceptFriends.as_view()),
    url(r'maps/friends/?$', MapFriends.as_view()),
    url(r'maps/me/?$', MapMe.as_view()),
    url(r'^$', views.api_home, name="api_home"),
]