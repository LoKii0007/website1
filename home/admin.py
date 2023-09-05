from django.contrib import admin
from .models import ProductType, Inquiry,Contact, Products

# Register your models here.

admin.site.register(ProductType)
admin.site.register(Contact)
admin.site.register(Inquiry)
admin.site.register(Products)