from django.shortcuts import render, redirect
from .forms import ContactUsForm


def home(request):
    return render(request, 'home/home.html')


def about_us(request):
    return render(request, 'home/about_us.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = ContactUsForm()
    return render(request, 'home/contact_us.html', {'form': form})
