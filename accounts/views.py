from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, ProductDetail, ProductDetailImage

# Simple pages
def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

# Index page
def index(request):
    ObjDTproduct = Product.objects.all()
    DTCategory = Category.objects.all()
    
    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': DTCategory
    }
    return render(request, 'electro/index.html', context)

def laptopSection(request):
    ObjDTproduct = Product.objects.all()
    ObjDTCategory = Category.objects.all()
    
    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': ObjDTCategory
    }
    return render(request, 'electro/laptop.html', context)


def smartphone_section(request):
    categories = Category.objects.all()
    
    # Get all products
    products = Product.objects.all()
    
    # Top selling products (example: latest 3 products)
    top_selling_products = Product.objects.order_by('-productDate')[:3]
    
    context = {
        'categories': categories,
        'products': products,
        'top_selling_products': top_selling_products,
    }
    return render(request, 'electro/smartphone.html', context)
# Blank page
def blank(request):
    return render(request, 'electro/blank.html')

# Product list page
def product(request):
    return render(request, 'electro/product.html')


# Product detail page
def productDetail(request, pk):
    DTCategory = Category.objects.all()
    DTProductDetail = get_object_or_404(Product, id=pk)
    DTProductDetailImage = ProductDetailImage.objects.filter(productID=pk)
    DTProductDetailInfo = ProductDetail.objects.filter(productID=pk)
    
    context = {
        'ObjDTCategory': DTCategory,
        'ObjDTProductDetail': DTProductDetail,
        'ObjDTProductDetailInfo': DTProductDetailInfo,
        'ObjDTProductDetailImage': DTProductDetailImage,
    }
    return render(request, 'electro/productDetail.html', context)

# Store page
def store(request):
    return render(request, 'electro/store.html')

# Checkout page
def checkout(request):
    return render(request, 'electro/checkout.html')

# Hot deals page
def HotDeal(request):
    return render(request, 'electro/HotDeal.html')

# Categories page
def Categories(request):
    return render(request, 'electro/categories.html')

# Category specific pages
def laptop(request):
    return render(request, 'electro/laptop.html')

def cameras(request):
    return render(request, 'electro/cameras.html')

def smartphone(request):
    return render(request, 'electro/smartphone.html')

def accessories(request):
    return render(request, 'electro/accessories.html')

# Cart functions
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
        cart[str(product_id)]['total'] = cart[str(product_id)]['quantity'] * cart[str(product_id)]['price']
    else:
        product_obj = get_object_or_404(Product, id=product_id)
        cart[str(product_id)] = {
            'productName': product_obj.productName,
            'price': float(product_obj.price),
            'quantity': 1,
            'total': float(product_obj.price),
            'image': product_obj.productImage.url if product_obj.productImage else ''
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
