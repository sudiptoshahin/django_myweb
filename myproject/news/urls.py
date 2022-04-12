from django.conf.urls import url
from news import views


urlpatterns = [

    url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),

    url(r'^panel/news/list/$', views.news_list, name='news_list'),

    url(r'^panel/news/add/$', views.news_add, name='news_add'),

    url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_del, name='news_delete'),

    
]