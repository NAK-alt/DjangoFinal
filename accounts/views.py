
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def index(request):
    return render(request,'electro/index.html')

def blank(request):
    return render(request,'electro/blank.html')

def product(request):
    return render(request,'electro/product.html')

def store(request):
    return render(request,'electro/store.html')

def checkout(request):
    return render(request,'electro/checkout.html')

def HotDeal(request):
    return render(request,'electro/HotDeal.html')

def Categories(request):
    return render(request,'electro/categories.html')

def product(request):
    return render(request,'electro/product.html')

def laptop(request):
    return render(request,'electro/laptop.html')

def cameras(request):
    return render(request,'electro/cameras.html')

def smartphone(request):
    return render(request,'electro/smartphone.html')

def accessories(request):
    return render(request,'electro/accessories.html')
