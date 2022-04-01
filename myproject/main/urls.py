from django.conf.urls import url
from main import views


urlpatterns = [

    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
]