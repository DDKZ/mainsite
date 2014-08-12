from django.db import models
from django.contrib.auth.models import User
from aspc.activityfeed.signals import new_activity, delete_activity
import datetime

class BookSale(models.Model):
    CONDITIONS = (
        (0, "like new"),
        (1, "very good"),
        (2, "good"),
        (3, "usable"),
    )

    # See http://www.pomona.edu/administration/sustainability/programs/recoop.aspx
    # Record these so ReCoop listings can be disabled on these days
    RECOOP_SALE_DATES = [
        datetime.date(2014, 8, 31),
        datetime.date(2014, 9, 1),
        datetime.date(2014, 9, 2),
        datetime.date(2014, 9, 3),
        datetime.date(2014, 9, 4)
    ]

    """Model representing a sale of a textbook"""
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255, verbose_name="Author(s)")
    isbn = models.CharField(max_length=20, null=True, blank=True, verbose_name="ISBN")
    edition = models.CharField(max_length=30, null=True, blank=True)
    condition = models.IntegerField(choices=CONDITIONS)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_recoop = models.BooleanField(default=False)
    recoop_id = models.IntegerField(unique=True, null=True)

    seller = models.ForeignKey(User, related_name="book_sales_set")
    buyer = models.ForeignKey(User, null=True, blank=True, related_name="book_purchases_set")

    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['posted']

    def __unicode__(self):
        return u"BookSale: {0} by {1} ({2})".format(self.title, self.authors, self.seller.username)

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(BookSale, self).save(*args, **kwargs)
        if created and not self.is_recoop:
            new_activity.send(sender=self, category="sagelist", date=self.posted)

    def delete(self, *args, **kwargs):
        delete_activity.send(sender=self)
        super(BookSale, self).delete(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('sagelist_detail', [self.id])

    @property
    def is_frozen(self):
        return self.is_recoop and datetime.date.today() in self.RECOOP_SALE_DATES