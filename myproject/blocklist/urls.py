from __future__ import unicode_literals
from . import views
from django.urls import path, re_path

urlpatterns = [

    path('blocklist/', views.block_list, name='block_list'),

    path('blocklist/add/ip/', views.add_blocked_ip, name='add_blocked_ip'),

    re_path(r'^blocklist/del/ip/(?P<pk>\d+)/$', views.del_blocked_ip, name='del_blocked_ip'),
]