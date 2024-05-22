from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.contrib.auth.models import User
from .models import Product, ProductType


class ProductAdmin(admin.ModelAdmin):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
