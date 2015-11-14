from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GeoUser(models.Model):
    user = models.OneToOneField(User, related_name="geouser", null=True, blank=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=10, default=-117.71008)
    latitude = models.DecimalField(decimal_places=6, max_digits=10, default=34.10079)
    friends = models.ManyToManyField("self")
    requests = models.ManyToManyField("self",related_name="requested_set")

    def __str__(self):
        return self.user.username


