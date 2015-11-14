from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GeoUser(models.Model):
    user = models.ForeignKey(User)
    longitude = models.DecimalField()
    latitude = models.DecimalField()
    friends = models.ManyToManyField("self",null=True,blank=True)
