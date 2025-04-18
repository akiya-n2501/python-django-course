from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
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


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        context["message_type"] = "detail"
        return context


class BlogEditView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_form.html"

    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy("blog:edit_done")

    def get_context_data(self, **kwargs):
        context = super(BlogEditView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        context["message_type"] = "edit"
        return context


def edit_done(request):
    # 更新処理が正常終了した場合に呼ばれるテンプレートを指定
    category_list = Category.objects.all()
    return render(request, "blog/edit_done.html", {"category_list": category_list})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
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


class CategoryView(ListView):
    """
    カテゴリ名でフィルタ検索
    """

    model = Blog
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        """
        カテゴリでの絞り込み
        """
        category_name = self.kwargs["category"]
        queryset = Blog.objects.filter(
            # 外部参照先の列名を指定する場合はアンダースコア２つ
            category__category_name=category_name
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class SearchPostView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        """
        request.GETにはGETリクエストのパラメータが含まれています。
        request.GET.get("q", None)でqパラメータの値を取得し、
        値が存在しない場合はNoneを取得します。
        """
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = Blog.objects.filter(
                Q(title__icontains=query) | Q(category__category_name__icontains=query)
            )
            return qs

        else:
            qs = Blog.objects.all()
            return qs

    def get_context_data(self, **kwargs):
        context = super(SearchPostView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context
