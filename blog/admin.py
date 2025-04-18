from django.contrib import admin

# Register your models here.
from blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "postdate", "category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
