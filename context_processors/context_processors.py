from product.models import Category as ProductCategory
from blog.models import Article, Category as BlogCategory


def product_sidebar(request):
    product_category = ProductCategory.objects.all()
    return {'product_category': product_category}


def blog_sidebar(request):
    article_category = BlogCategory.objects.all()
    latest_articles = Article.objects.filter(status='published').order_by('-created_at')[:3]
    if hasattr(request, 'resolver_match') and request.resolver_match.url_name == 'article_detail':
        article_slug = request.resolver_match.kwargs.get('slug')
        if article_slug:
            current_article = Article.objects.filter(slug=article_slug).first()
            if current_article:
                latest_articles = [article for article in latest_articles if article.id != current_article.id]
    return {'article_category': article_category, 'latest_articles': latest_articles}


def cart_item_count(request):
    cart = request.session.get('cart', {})
    total_items = sum(item['quantity'] for item in cart.values())
    return {'cart_item_count': total_items}
