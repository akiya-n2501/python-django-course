from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import BlogForm
from .models import Blog, Category


def index(request):
    print("index関数を使ってTOP画面を表示します。")
    return render(request, "blog/index.html")


class IndexView(TemplateView):
    # TOP画面を表示するクラス
    template_name = "blog/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("IndexViewを使ってTOP画面を表示します。")
        return self.render_to_response(context)


class BlogListView(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy("blog:create_done")

    def get_context_data(self, **kwargs):
        context = super(BlogCreateView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        context["message_type"] = "create"
        return context


def create_done(request):
    # 登録処理が正常終了した場合に呼ばれる
    category_list = Category.objects.all()
    return render(request, "blog/create_done.html", {"category_list": category_list})


class BlogDetailView(DeleteView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        context["message_type"] = "edit"
        return context


class BlogEditView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_form.html"

    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy("blog:edit_done")

    def get_context_data(self, **kwargs):
        context = super(BlogEditView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


def edit_done(request):
    # 更新処理が正常終了した場合に呼ばれるテンプレートを指定
    category_list = Category.objects.all()
    return render(request, "blog/edit_done.html", {"category_list": category_list})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:delete_done")

    def get_context_data(self, **kwargs):
        context = super(BlogDeleteView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


def delete_done(request):
    category_list = Category.objects.all()
    return render(request, "blog/delete_done.html", {"category_list": category_list})
