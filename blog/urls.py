from django.urls import path

from .views import (
    BlogCreateView,
    BlogDetailView,
    BlogEditView,
    BlogListView,
    IndexView,
    create_done,
    edit_done,
    index,
)

app_name = "blog"

urlpatterns = [
    path("index/", index, name="index"),
    path("index_class", IndexView.as_view(), name="index_class"),
    path("", BlogListView.as_view(), name="blog_list"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("create_done/", create_done, name="create_done"),
    path("detail/<int:pk>", BlogDetailView.as_view(), name="detail"),
    path("edit/<int:pk>", BlogEditView.as_view(), name="edit"),
    path("edit_done/", edit_done, name="edit_done"),
]
