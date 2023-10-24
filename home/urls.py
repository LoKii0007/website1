from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.urls import re_path


admin.site.site_header = "Rao builders"
admin.site.site_title = "Rao builders"
admin.site.index_title = "Welcome to Rao builders"  

# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r"^static/(?P<path>.*)$", views.serve),
#     ]

urlpatterns = [
    path("", views.home, name='home'),
    path("productview<int:pid>", views.productview, name='productview'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('inquiry', views.handleInquiry, name='handleInquiry'),
    path('contact', views.contact, name='contact'),
    path("product", views.products, name='products'),
    path('location', views.location, name='location'),
]
