from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse


STATUS = (
    ('draft', 'پیش نویس'),
    ('published', 'منتشر شود'),
)


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name='نامک')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_absolute_url(self):
        return reverse('blog:category_article_list', args=[self.slug])

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده مقاله')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='articles', verbose_name='دسته بندی مربوطه')
    title = models.CharField(max_length=200, unique=True, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, verbose_name='نامک')
    description = models.TextField(verbose_name='متن مقاله')
    image = models.ImageField(upload_to='images/articles', blank=True, null=True, verbose_name='تصویر مقاله')
    status = models.CharField(choices=STATUS, max_length=10, verbose_name='وضعیت')
    views = models.IntegerField(default=0, editable=False, verbose_name='بازدید')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def article_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')
        return format_html(f'<h3 style="color: red">تصویر ندارد</h3>')

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله مربوطه')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_comments', verbose_name='نویسنده دیدگاه')
    body = models.TextField(verbose_name='متن دیدگاه')
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.article.title
