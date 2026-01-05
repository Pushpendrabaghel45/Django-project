from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .models import Product

# from products.models import Product, Category
from django.contrib.auth import logout
# Create your views here.
def home(request):
    return render(request, 'index.html')
        
def pages(request):
    return render(request, 'pages.html')

def shop(request):
    return render(request, 'shop.html')
       

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')





def admin_logout(request):
    logout(request)
    return redirect('home')
