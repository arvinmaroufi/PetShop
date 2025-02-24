from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.CartOrder)
class CartOrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'price', 'get_order_date_jalali', 'product_status', 'is_status']
    list_editable = ['product_status']

    @admin.display(description='تاریخ سفارش', ordering='order_date')
    def get_order_date_jalali(self, obj):
        return datetime2jalali(obj.order_date).strftime('%a, %d %b %Y')


@admin.register(models.CartOrderItem)
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'invoice_no', 'qty', 'price', 'total', 'product_status']
    list_editable = ['product_status']
