from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")

def our_services(request):
    return render(request, "our_services.html")