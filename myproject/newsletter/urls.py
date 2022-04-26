from django.urls import path, re_path
from . import views
urlpatterns = [

    path('panel/newsletter/add/', views.news_letter, name='news_letter'),

    path('panel/newsletter/emails/', views.news_letter_emails, name='news_letter_emails'),

    path('panel/newsletter/phones/', views.news_letter_phones, name='news_letter_phones'),

    re_path(r'^panel/newletter/delete/(?P<pk>\d+)/(?P<status>\d+)/$', views.news_letter_txt_del, name='news_letter_del'),

]