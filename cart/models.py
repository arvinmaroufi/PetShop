from django.db import models
from django.contrib.auth.models import User
from product.models import Product


STATUS_CHOICE = (
    ("processing", "درحال پردازش"),
    ("shipped", "ارسال شد"),
    ("delivered", "تحویل داده شد"),
)


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    price = models.IntegerField(default=10000, verbose_name="قیمت کل")
    is_status = models.BooleanField(default=False, verbose_name="آیا پرداخت شده یا نه؟")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ سفارش")
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing", verbose_name="وضعیت محصول")

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return self.user.username


class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE, verbose_name="سفارش")
    item = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    invoice_no = models.CharField(max_length=200, verbose_name="شماره فاکتور")
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing", verbose_name="وضعیت محصول")
    qty = models.IntegerField(default=0, verbose_name="تعداد")
    price = models.IntegerField(default=10000, verbose_name="قیمت")
    total = models.IntegerField(default=100000, verbose_name="جمع کل")

    class Meta:
        verbose_name = "آیتم سفارش در سبد خرید"
        verbose_name_plural = "آیتم ‌های سفارش در سبد خرید"

    def __str__(self):
        return self.item.title

