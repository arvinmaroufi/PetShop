from product.models import Product, Category


def product_sidebar(request):
    # latest_articles = Article.objects.all().order_by('-updated')[:3]
    categories = Category.objects.all()
    return {'categories': categories}