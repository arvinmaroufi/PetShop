from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=100, allow_unicode=True, verbose_name='نامک')
    image = models.ImageField(upload_to='images/category', null=True, blank=True, verbose_name='تصویر دسته بندی')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def category_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')
        return format_html(f'<h3 style="color: red">تصویر ندارد</h3>')

    def get_absolute_url(self):
        return reverse('product:category_product_list', args=[self.slug])

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی مربوطه')
    title = models.CharField(max_length=300, unique=True, verbose_name='عنوان محصول')
    slug = models.SlugField(max_length=300, unique=True, allow_unicode=True, verbose_name='نامک')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    full_description = models.TextField(verbose_name='توضیحات کامل')
    price = models.IntegerField(verbose_name='قیمت محصول')
    stock_count = models.IntegerField(verbose_name='تعداد موجود')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def product_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')
        return format_html(f'<h3 style="color: red">تصویر ندارد</h3>')

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='محصول مربوطه')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='نویسنده دیدگاه')
    body = models.TextField(verbose_name='متن دیدگاه')
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    popular_comment = models.BooleanField(default=False, verbose_name='آیا کامنت به کامنت های محبوب اضافه شود؟')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.product.title

