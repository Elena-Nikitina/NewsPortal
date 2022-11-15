from django.forms import ModelForm
from .models import Post
from django.core.exceptions import ValidationError

TITLE_MIN_LENGTH = 10
TEXT_MIN_LENGTH = 50


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'categoryType', 'postCategory', 'text']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if text is not None and len(text) < TEXT_MIN_LENGTH:
            raise ValidationError({
                "title": f"Текст не может быть менее {TEXT_MIN_LENGTH} символов."
            })
        if title == text:
            raise ValidationError(
                "Текст не может совпадать с названием."
            )
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data["title"]
        if title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return title