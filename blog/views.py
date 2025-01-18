from django.shortcuts import render, get_object_or_404
from .models import Category, Article, Comment
from django.core.paginator import Paginator


def get_pages_to_show(current_page, total_pages):
    if total_pages <= 3:
        return list(range(1, total_pages + 1))

    if current_page <= 2:
        return [1, 2, 3, '...', total_pages]

    if current_page >= total_pages - 1:
        return [1, '...', total_pages - 2, total_pages - 1, total_pages]

    return [1, '...', current_page - 1, current_page, current_page + 1, '...', total_pages]


def article_list(request):
    articles = Article.objects.filter(status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 9)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'articles': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'blog/article_list.html', context)


def category_article_list(request, slug):
    category = Category.objects.get(slug=slug)
    articles = Article.objects.filter(category=category)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 9)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'category': category,
        'articles': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'blog/category_article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, author=request.user)
    session_key = f'article_{article.id}_viewed'
    if not request.session.get(session_key, False):
        article.views += 1
        article.save()
        request.session[session_key] = True
    context = {
        'article': article,
    }
    return render(request, 'blog/article_detail.html', context)


def article_search(request):
    articles_search = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=articles_search)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 9)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'articles': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'blog/article_list.html', context)
