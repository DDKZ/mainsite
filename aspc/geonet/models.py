from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GeoUser(models.Model):
    user = models.ForeignKey(User)
    longitude = models.DecimalField(decimal_places=6, max_digits=10)
    latitude = models.DecimalField(decimal_places=6, max_digits=10)
    friends = models.ManyToManyField("self",null=True,blank=True)
