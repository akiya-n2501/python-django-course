from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # admin
    path("management", admin.site.urls),
    # blog
    path("blog/", include("blog.urls")),
]
