from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Product
from .models import CartOrder, CartOrderItem
from django.contrib import messages
import random
from django.db import transaction


def get_cart_item_count(request):
    cart = request.session.get('cart', {})
    return sum(item['quantity'] for item in cart.values())


def get_cart(request):
    cart = request.session.get('cart', {})
    return cart


def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = Product.objects.get(id=product_id)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'title': product.title,
            'price': product.price,
            'quantity': 1,
            'image': product.image.url if product.image else None,
        }

    request.session['cart'] = cart
    return redirect('cart:cart_view')


def cart_view(request):
    cart = get_cart(request)
    total_price = 0
    total_items = 0
    cart_items_to_remove = []

    for product_id, item in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            item['stock_count'] = product.stock_count
            total_price += item['price'] * item['quantity']
            total_items += item['quantity']
        except Product.DoesNotExist:
            cart_items_to_remove.append(product_id)

    for product_id in cart_items_to_remove:
        del cart[product_id]

    request.session['cart'] = cart

    return render(request, 'cart/cart.html', {'cart': cart, 'total_price': total_price, 'total_items': total_items})


def update_cart(request, product_id, action):
    cart = get_cart(request)
    product = Product.objects.get(id=product_id)

    if str(product_id) in cart:
        if action == 'increase':
            if cart[str(product_id)]['quantity'] < product.stock_count:
                cart[str(product_id)]['quantity'] += 1
        elif action == 'decrease':
            cart[str(product_id)]['quantity'] -= 1
            if cart[str(product_id)]['quantity'] <= 0:
                del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart:cart_view')


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "سبد خرید شما خالی است! لطفاً حداقل یک محصول را اضافه کنید.")
        return redirect('cart:cart_view')
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')

        invoice_no = random.randint(1000000000, 9999999999)

        try:
            with transaction.atomic():
                order = CartOrder.objects.create(
                    user=request.user,
                    price=total_price,
                    is_status=True,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address=address,
                    zipcode=zipcode,
                )

                for product_id, item in cart.items():
                    product = Product.objects.get(id=product_id)
                    if product.stock_count < item['quantity']:
                        raise ValueError(f"موجودی محصول {product.title} کافی نیست.")

                    product.stock_count -= item['quantity']
                    product.save()

                    CartOrderItem.objects.create(
                        order=order,
                        item=product,
                        invoice_no=invoice_no,
                        qty=item['quantity'],
                        price=item['price'],
                        total=item['price'] * item['quantity'],
                    )

                request.session['cart'] = {}
                messages.success(request, "سفارش شما با موفقیت ثبت شد و موجودی محصولات به‌روزرسانی شد.")
                return redirect('cart:cart_view')

        except ValueError as e:
            messages.error(request, str(e))
            return redirect('cart:cart_view')
        except Exception as e:
            messages.error(request, "خطایی در پردازش سفارش رخ داد. لطفاً دوباره تلاش کنید.")
            return redirect('cart:cart_view')

    return render(request, 'cart/checkout.html', {'total_price': total_price, 'cart': cart})