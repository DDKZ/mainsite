# django imports
from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=120)
    # author = models.CharField(max_length=30)
    # contact = models.CharField(max_length=30)
    price = models.CharField(max_length=6)
    content = models.TextField()
    image = models.ImageField(upload_to='listings_pics', blank=True, null=True)

    seller = models.ForeignKey(User, related_name="item_sales_set")
    # buyer = models.ForeignKey(User, null=True, blank=True, related_name="item_purchases_set")
    sold = models.BooleanField(default=False)
    posted = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return u'/listings/%d' % self.id