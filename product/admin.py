from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.Category)
class CategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'category_image', 'get_created_jalali']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')


@admin.register(models.Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['short_title', 'category', 'price', 'stock_count', 'product_image', 'get_created_jalali']
    prepopulated_fields = {'slug': ('title',)}

    def short_title(self, obj):
        if len(obj.title) > 20:
            return obj.title[:20] + '...'
        return obj.title
    short_title.short_description = 'نام محصول'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')


@admin.register(models.Comment)
class CommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['short_product_title', 'author', 'short_body', 'get_created_jalali', 'popular_comment', 'active']
    list_editable = ['active', 'popular_comment']

    def short_product_title(self, obj):
        if len(obj.product.title) > 10:
            return obj.product.title[:10] + '...'
        return obj.product
    short_product_title.short_description = 'محصول مربوطه'

    def short_body(self, obj):
        if len(obj.body) > 20:
            return obj.body[:20] + '...'
        return obj.body
    short_body.short_description = 'متن دیدگاه'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y - %H:%M:%S')
