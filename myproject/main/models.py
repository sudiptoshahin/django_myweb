from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):

    name = models.CharField(max_length=20)
    about = models.TextField(default='-')
    fb = models.CharField(default='-', max_length=50)
    tw = models.CharField(default='-', max_length=50)
    yt = models.CharField(default='-', max_length=50)
    tel = models.CharField(default='-', max_length=50)
    link = models.CharField(default='-', max_length=50)

    set_name = models.CharField(default='-', max_length=50)

    picname = models.TextField(default='')
    picurl = models.TextField(default='')

    picname2 = models.TextField(default='')
    picurl2 = models.TextField(default='')

    def __str__(self):
        return self.set_name + ' | ' + str(self.pk)

