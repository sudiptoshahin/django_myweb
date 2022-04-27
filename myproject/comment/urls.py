from django.urls import path, re_path
from . import views

urlpatterns = [

    re_path(r'^comment/add/news/(?P<pk>\d+)/$', views.news_cm_add, name='news_cm_add'),

    path('comments/list/', views.news_cm_list, name='news_comments'),

    re_path(r'^comment/delete/(?P<pk>\d+)/$', views.news_cm_del, name='news_comment_del'),

    re_path(r'^comment/confirmed/(?P<pk>\d+)/$', views.news_cm_confirmed, name='news_comment_confirmed'),

]