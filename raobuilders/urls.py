from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r"^static/(?P<path>.*)$", views.serve),
#     ]