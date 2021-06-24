from django.db import models


class Post(models.Model):
    title = models.CharField('Название', max_length=50)
    post = models.TextField('Описание')
    author = models.CharField('Автор', max_length=25)
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Tag(models.Model):
    name = models.CharField('Название', max_length=25, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
