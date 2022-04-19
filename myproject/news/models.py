from django.db import models

# Create your models here.


class News(models.Model):

    name = models.CharField(max_length=120)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default='00:00')
    picname = models.TextField()
    picurl = models.TextField(default='-')
    writer = models.CharField(max_length=20)
    catname = models.CharField(max_length=50, default='-')
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tag = models.TextField(default='-')

    def __str__(self):
        return self.name

