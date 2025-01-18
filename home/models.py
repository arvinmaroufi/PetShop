from django.db import models
from django.utils.html import format_html


class ContactUs(models.Model):
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    subject = models.CharField(max_length=100, verbose_name='موضوع')
    message = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return f'{self.email} - {self.subject}'


class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name='سوال')
    answer = models.TextField(verbose_name='جواب')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = "سوال متداول"
        verbose_name_plural = "سوالات متداول"

    def __str__(self):
        return self.question


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/gallery', verbose_name='تصویر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری ها"

    def gallery_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="70px" height="50px">')

