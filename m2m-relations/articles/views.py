from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles_objects = Article.objects.all().order_by(ordering)
    context = {'object_list': articles_objects}

    return render(request, template, context)
