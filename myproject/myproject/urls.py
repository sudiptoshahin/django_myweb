from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),

    # main
    url(r'', include('main.urls')),
    # news
    url(r'', include('news.urls')),
    # category
    url(r'', include('cat.urls')),
    # subcategory
    url(r'', include('subcat.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
