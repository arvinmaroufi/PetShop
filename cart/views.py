from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Product
from .models import CartOrder, CartOrderItem


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
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart/cart.html', {'cart': cart, 'total_price': total_price})


def update_cart(request, product_id, action):
    cart = get_cart(request)

    if str(product_id) in cart:
        if action == 'increase':
            cart[str(product_id)]['quantity'] += 1
        elif action == 'decrease':
            cart[str(product_id)]['quantity'] -= 1
            if cart[str(product_id)]['quantity'] <= 0:
                del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart:cart_view')



@login_required
def checkout(request):
    # Implement checkout logic here
    pass
