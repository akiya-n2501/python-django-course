from django.contrib import admin

# Register your models here.
from blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "postdate", "category")


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
