from django.conf.urls import url
from main import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    # url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),

    # back-end url
    url(r'^panel/$', views.panel, name='panel'),
]