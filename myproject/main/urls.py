# from django.conf.urls import url
from django.urls import path
from main import views


urlpatterns = [

    path('', views.home, name='home'),
    # url(r'^home/$', views.home, name='home'),
    path('about/', views.about, name='about'),

    # back-end url
    path('panel/', views.panel, name='panel'),

    #login
    path('login/', views.my_login, name='login'),

    # logout
    path('logout/', views.my_logout, name='logout'),

    # site settings
    path('panel/setting/', views.site_setting, name='site_setting'),
]