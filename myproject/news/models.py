from __future__ import unicode_literals
from email.policy import default
from django.db import models

# Create your models here.


class News(models.Model):

    name = models.CharField(max_length=20)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    pic = models.TextField()
    writer = models.CharField(max_length=20)
    catname = models.CharField(max_length=50, default='-')
    catid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)

    def __str__(self):
        return self.name

