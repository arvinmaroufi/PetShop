from django.db import models


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
