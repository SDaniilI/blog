from .models import Post, Tag
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "post", "author", "tag"]
        widgets = {
            "title": TextInput(attrs={
                 'class': 'form-control',
                 'placeholder': 'Введите название',
            }),
            "post": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора поста',
            }),
        }