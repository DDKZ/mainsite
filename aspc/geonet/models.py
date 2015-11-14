from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
import autocomplete_light
# Create your models here.

class GeoUser(models.Model):
    user = models.OneToOneField(User, related_name="geouser")
    longitude = models.DecimalField(decimal_places=6, max_digits=10, default=-117.71008)
    latitude = models.DecimalField(decimal_places=6, max_digits=10, default=34.10079)
    friends = models.ManyToManyField("self")
    requests = models.ManyToManyField("self",related_name="requested_set")

    def __str__(self):
        return self.user.username

class GeoUserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    class Meta:
        model = GeoUser
        fields = ('username', 'first_name', 'last_name', 'latitude', 'longitude')

    def create(self, validated_data):
        username = validated_data.pop('username')
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('latitude')
        user = User.objects.filter(username=username).first()
        geouser = GeoUser.objects.create(user=user, latitude=latitude, longitude=longitude)
        return geouser

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        return instance