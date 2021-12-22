from django.shortcuts import render
from articles.models import Article, Relationship


def articles_list(request):
    template = 'articles/news.html'
    art = Article.objects.all()
    context = {'object_list':art}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    class Meta:
        ordering = '-published_at'
        
    return render(request, template, context)


