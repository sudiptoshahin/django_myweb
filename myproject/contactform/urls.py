
from django.urls import path
from . import views

urlpatterns = [

    path('contact/submit/', views.contact_add, name='contact_add'),

    # contact list
    path('panel/contactform/', views.contact_show, name='contact_show'),
    # contact del
    path(r'^panel/contactform/del/(?P<pk>\d+)/$', views.contact_del, name='contact_del'),
]