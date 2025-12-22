from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'product_detail.html', {'product': product})


def profile(request):
    return render(request, 'profile.html')


def request_time(request):
    return render(request, 'request_time.html')
