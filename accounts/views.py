
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def index(request):
    ObjDTproduct = Product.objects.all()
    context = {
        'ObjDTproduct': ObjDTproduct  # <-- Changed to uppercase 'P'
    }
    return render(request,'electro/index.html', context)

def blank(request):
    return render(request,'electro/blank.html')

def product(request):
    return render(request,'electro/product.html')

def productDetail(request, pk):
    DTProductDetail = Product.objects.get(id=pk)
    DTProductDetailImage = ProductDetailImage.objects.filter(productID=pk)
    context = {
        'ObjDTProductDetail':DTProductDetail,
        'ObjDTProductDetailImage' :DTProductDetailImage
    }
    return render(request, 'electro/productDetail.html',context)

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

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
        cart[str(product_id)]['total'] = cart[str(product_id)]['quantity'] * cart[str(product_id)]['price']
    else:
        product = product.objects.get(id=product_id)
        cart[str(product_id)] = {
            'productName': product.productName,
            'price': float(product.price),
            'quantity': 1,
            'total': float(product.price) * 1,
            'image': product.productImage.url if product.productImage else ''
        }

    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'Ogani/shoping-cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')

def checkout_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())

    return render(request, 'Ogani/checkout.html', {
        'cart': cart,
        'total_price': total_price,
    })



