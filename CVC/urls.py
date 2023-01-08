from django.conf import settings
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('snack/', snack),
    path('any4/', any4),
    path('any4/get_positions', get_positions),
    path('cards/',include('mobile.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
