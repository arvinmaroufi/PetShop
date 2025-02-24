from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from cart.models import CartOrder
from .forms import ProfileEditForm
from django.contrib.auth import logout, update_session_auth_hash
from accounts.forms import ChangePasswordForm
from django.contrib import messages
import product.models
import blog.models


@login_required
def dashboard(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    completed_orders = CartOrder.objects.filter(user=user, is_status=True)
    recent_orders = CartOrder.objects.filter(user=user).order_by('-order_date')[:5]

    product_comments_count = product.models.Comment.objects.filter(author=user).count()
    article_comments_count = blog.models.Comment.objects.filter(author=user).count()
    total_comments_count = product_comments_count + article_comments_count
    context = {
        'profile': profile,
        'completed_orders': completed_orders,
        'recent_orders': recent_orders,
        'total_comments_count': total_comments_count,
    }
    return render(request, 'dashboard/home.html', context)


@login_required
def order_list(request):
    user = request.user
    orders = CartOrder.objects.filter(user=user).order_by('-order_date')
    context = {
        'orders': orders
    }
    return render(request, 'dashboard/orders.html', context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(CartOrder, order_id=order_id, user=request.user)
    order_items = order.cartorderitem_set.all()
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'dashboard/order_detail.html', context)


@login_required
def edit_profile(request, username):
    user = request.user
    profiles = Profile.objects.get(user=user)
    profile = get_object_or_404(Profile, user__username=username)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'dashboard/profile.html', {'profiles': profiles, 'form': form})


@login_required
def setting(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']

            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                logout(request)
                messages.success(request, 'رمز عبور شما با موفقیت تغییر یافت. لطفاً با رمز عبور جدید وارد شوید.')
                return redirect('account:login')
            else:
                form.add_error('old_password', 'رمز عبور فعلی نادرست است.')
    else:
        form = ChangePasswordForm()

    return render(request, 'dashboard/settings.html', {'form': form})
