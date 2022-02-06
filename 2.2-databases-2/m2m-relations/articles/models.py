from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32, default='Разное', verbose_name='Название рубрики')

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрикатор'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag, related_name='articles', through='RelationShip')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class RelationShip(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='relationships')
    heading = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='relationships', verbose_name='Выбор рубрики',)
    is_main = models.BooleanField(default=False, verbose_name='Основная рубрика')

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'РУБРИКИ'
