from django.db import models

# Create your models here.


class Category(models.Model):
    # フィールド名の定義
    category_name = models.CharField(
        verbose_name="カテゴリ名", max_length=100, unique=True
    )
    category_image = models.ImageField(verbose_name="カテゴリ画像", upload_to="images/")

    class Meta:
        # テーブル名
        db_table = "category"
        verbose_name = "カテゴリ名"
        verbose_name_plural = "カテゴリ名"

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=100)
    content = models.TextField(verbose_name="内容")
    postdate = models.DateField(verbose_name="投稿日", auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="カテゴリ"
    )

    class Meta:
        db_table = "blog"
        verbose_name = "ブログ記事"
        verbose_name_plural = "ブログ記事"

    def __str__(self):
        return self.title
