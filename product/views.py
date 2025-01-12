from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Comment
from django.core.paginator import Paginator


def get_pages_to_show(current_page, total_pages):
    if total_pages <= 3:
        return list(range(1, total_pages + 1))

    if current_page <= 2:
        return [1, 2, 3, '...', total_pages]

    if current_page >= total_pages - 1:
        return [1, '...', total_pages - 2, total_pages - 1, total_pages]

    return [1, '...', current_page - 1, current_page, current_page + 1, '...', total_pages]


def product_list(request):
    products = Product.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(products, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'products': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'product/product_list.html', context)


def category_product_list(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    page_number = request.GET.get('page')
    paginator = Paginator(products, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'category': category,
        'products': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'product/category_product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    similar_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    if request.method == 'POST':
        body = request.POST.get('body')
        Comment.objects.create(body=body, product=product, author=request.user)
    context = {
        'product': product,
        'similar_products': similar_products,
    }
    return render(request, 'product/product_detail.html', context)


def product_search(request):
    products_search = request.GET.get('search')
    products = Product.objects.filter(title__icontains=products_search)
    page_number = request.GET.get('page')
    paginator = Paginator(products, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    context = {
        'products': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'product/product_list.html', context)
