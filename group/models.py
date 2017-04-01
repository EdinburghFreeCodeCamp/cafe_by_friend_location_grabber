from __future__ import unicode_literals
from cafe.models import Cafe
from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    chosen_cafe = models.ForeignKey(Cafe, null=True, blank=True)

class Member(models.Model):
    post_code = models.CharField(max_length=10)
    group = models.ForeignKey(Group)
