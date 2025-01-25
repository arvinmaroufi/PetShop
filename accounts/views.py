from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, LoginForm, ChangePasswordForm
from django.contrib import messages


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # تنظیم پسورد
            user.save()  # ذخیره کاربر
            return redirect('account:login')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')


@login_required
def change_password(request):
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

    return render(request, 'accounts/change_password.html', {'form': form})
