from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),

    # main
    url(r'', include('main.urls')),
    url(r'', include('news.urls')),
]
