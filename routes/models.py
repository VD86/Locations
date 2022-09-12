from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    '''
    Модель класса маршрутов.
    '''

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Автор статьи',
                               blank=True, null=True)
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name = 'Заголовок')
    image = models.ImageField(upload_to='static', verbose_name = 'Фото')
    desc = models.TextField(verbose_name = 'Описание')
    #slug = models.SlugField(max_length=255, unique =True, verbose_name = 'URL')
    publish = models.DateTimeField(default=timezone.now, verbose_name = 'Публикация')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['-publish', 'title']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name = 'Статья',
                             related_name='comments_posts', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Автор комментария',
                               blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Текст комментария:')
    status = models.BooleanField(verbose_name = 'Активность статьи', default=False)

    class Meta:
        verbose_name_plural = 'Комментарии'
        ordering = ('-created',)

    def __str__(self):
        return self.name, self.post