# from django.conf.urls import url
from django.urls import path, re_path
from news import views


urlpatterns = [

    re_path(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),

    re_path(r'^urls/(?P<pk>\d+)/$', views.news_detail_short, name='news_detail_short'),

    path('panel/news/list/', views.news_list, name='news_list'),

    path('panel/news/add/', views.news_add, name='news_add'),

    # url(dj-1) => re_path (dj-4)
    re_path(r'^panel/news/del/(?P<pk>\d+)/$', views.news_del, name='news_delete'),

    re_path(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),

    re_path(r'^panel/news/publish/(?P<pk>\d+)/$', views.news_publish, name='news_publish'),

    
]