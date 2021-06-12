from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "author", "tag"]
        widgets = {
            "title": TextInput(attrs={
                 'class': 'form-control',
                 'placeholder': 'Введите название',
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора поста',
            }),
            "tag": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тег',
            }),
        }