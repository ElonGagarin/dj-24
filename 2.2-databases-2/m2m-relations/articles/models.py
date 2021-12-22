from django.db import models
from django.utils.translation import to_language

class TagList(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    articles = models.ManyToManyField(TagList, through='Relationship', related_name='scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Relationship(models.Model):    
    scopes = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(TagList, on_delete=models.CASCADE, related_name='tag')
    is_main = models.BooleanField(default=False)
