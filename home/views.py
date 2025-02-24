from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import FAQ, Gallery
from product.models import Category, Product, Comment
from blog.models import Article


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:5]
    popular_comments = Comment.objects.filter(popular_comment=True)[:4]
    popular_articles = Article.objects.filter(status='published').order_by('-views')[:4]
    context = {
        'categories': categories,
        'products': products,
        'popular_comments': popular_comments,
        'popular_articles': popular_articles,
    }
    return render(request, 'home/home.html', context)


def about_us(request):
    faq_list = FAQ.objects.all()
    product_count = Product.objects.count()
    context = {
        'faq_list': faq_list,
        'product_count': product_count,
    }
    return render(request, 'home/about_us.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = ContactUsForm()
    return render(request, 'home/contact_us.html', {'form': form})


def gallery(request):
    galleries = Gallery.objects.all()
    context = {
        'galleries': galleries
    }
    return render(request, 'home/gallery.html', context)
    