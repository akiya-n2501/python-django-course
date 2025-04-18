from typing import ClassVar

from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """

    class Meta:
        # フォーム画面に利用したいデータのモデル名を指定
        model = Blog
        # フォーム画面に表示したい列名を指定。
        fields: ClassVar[list[str]] = ["title", "content", "category"]
        # 全ての列名を表示させたい場合、`__all__`だが、今回は投稿日はいらないため。
