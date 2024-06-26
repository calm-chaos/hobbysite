from django.contrib import admin
from .models import *


class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory


class PostAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
