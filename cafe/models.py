from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cafe(models.Model):
    name = models.CharField(max_length=30)
    locationx = models.DecimalField(max_digits=20, decimal_places=19)
    locationy = models.DecimalField(max_digits=20, decimal_places=19)
    address_line1  = models.CharField(max_length=100)
    address_line2 = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)

    class Meta:
        unique_together = (('locationx', 'locationy'))


class Comment(models.Model):
    cafe = models.ForeignKey(Cafe)
    rating_choices = ((i,i) for i in [0,1,2,3,4,5])
    rating = models.IntegerField(choices=rating_choices)
    comment = models.CharField(null=True, blank=True, max_length=250)
