# from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),

    # main
    path('', include('main.urls')),
    # news
    path('', include('news.urls')),
    # category
    path('', include('cat.urls')),
    # subcategory
    path('', include('subcat.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
