from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    author = models.CharField('Автор', max_length=25)
    tag = models.CharField('Теги', max_length=25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


# class Tags:
#     name = ...
