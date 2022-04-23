from django.contrib import admin
from .models import Main
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Register your models here.
admin.site.register(Main)
admin.site.register(Permission)
admin.site.register(ContentType)