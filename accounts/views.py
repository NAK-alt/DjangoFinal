from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, ProductDetail, ProductDetailImage, BillingDetail
import random # <-- IMPORT THIS

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
    product_list = list(ObjDTproduct)
    random.shuffle(product_list)
    
    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTproduct_shuffled': product_list,
        'ObjDTCategory': DTCategory
    }
    return render(request, 'electro/index.html', context)
def All(request):
    ObjDTCategory = Category.objects.all()

    # Check if user clicked a category
    selected_category = request.GET.get('category')

    if selected_category:
        ObjDTproduct = Product.objects.filter(categoryID=selected_category)
    else:
        # Default: show all
        ObjDTproduct = Product.objects.all()

    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': ObjDTCategory,
    }
    return render(request, 'electro/All.html', context)


def laptop(request):
    ObjDTCategory = Category.objects.all()
    ObjDTproduct = Product.objects.filter(categoryID__categoryName__iexact='Laptop')
    
    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': ObjDTCategory,
    }
    return render(request, 'electro/laptop.html', context)
def smartphone(request):
    ObjDTCategory = Category.objects.all()
    ObjDTproduct = Product.objects.filter(categoryID__categoryName__iexact='smartphone')
    
    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': ObjDTCategory,
    }
    return render(request, 'electro/smartphone.html', context)
def cameras(request):
    ObjDTCategory = Category.objects.all()
    ObjDTproduct = Product.objects.filter(categoryID__categoryName__iexact='camera')
    
    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': ObjDTCategory,
    }
    return render(request, 'electro/cameras.html', context)
def accessories(request):
    ObjDTCategory = Category.objects.all()
    ObjDTproduct = Product.objects.filter(categoryID__categoryName__iexact='accessories')
    
    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': ObjDTCategory,
    }
    return render(request, 'electro/accessories.html', context)

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

    category_pk = DTProductDetail.categoryID.id
    category_template_map = {
        1: 'electro/productSectionSmartphone.html',
        2: 'electro/productSectionlaptop.html',
        3: 'electro/productSectionCamera.html',
        4: 'electro/productSectionAccessories.html',
    }
    dynamic_template = category_template_map.get(
        category_pk,
        'electro/productSection.html'  # default
    )

    # FIX: only get details for the selected product
    DTProductDetailInfo = ProductDetail.objects.filter(productID=pk).first()

    # FIX: images related to the product
    DTProductDetailImage = ProductDetailImage.objects.filter(productID=pk)

    # Related products (optional)
    smartphone_products = Product.objects.filter(categoryID_id=1)
    laptop_products = Product.objects.filter(categoryID_id=2)
    camera_products = Product.objects.filter(categoryID_id=3)
    accessories_products = Product.objects.filter(categoryID_id=4)

    context = {
        'ObjDTCategory': DTCategory,
        'ObjDTProductDetail': DTProductDetail,
        'ObjDTProductDetailInfo': DTProductDetailInfo,
        'ObjDTProductDetailImage': DTProductDetailImage,
        'smartphone_products': smartphone_products,
        'laptop_products': laptop_products,
        'camera_products': camera_products,
        'accessories_products': accessories_products,
        'product_pk': pk,
        'category_pk': category_pk,
        'dynamic_template': dynamic_template,   # <-- important

    }

    return render(request, 'electro/productDetail.html', context)


# Store page
def store(request):
    return render(request, 'electro/store.html')

# Checkout page

# Hot deals page
def HotDeal(request):
    return render(request, 'electro/HotDeal.html')

# Categories page
def Categories(request):
    return render(request, 'electro/categories.html')


def checkout(request):
    return render(request, 'electro/checkout.html')

# Cart functionsfrom django.shortcuts import get_object_or_404, redirect

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    # Get the quantity submitted from the form
    quantity = int(request.POST.get('quantity', 1))  # default to 1 if not provided

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
        cart[str(product_id)]['total'] = cart[str(product_id)]['quantity'] * cart[str(product_id)]['price']
    else:
        product_obj = get_object_or_404(Product, id=product_id)
        cart[str(product_id)] = {
            'productName': product_obj.productName,
            'price': float(product_obj.price),
            'quantity': quantity,
            'total': float(product_obj.price) * quantity,
            'image': product_obj.productImage.url if product_obj.productImage else ''
        }

    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'electro/shoping-cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')

def checkout_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())
    return render(request, 'electro/checkout.html', {
        'cart': cart,
        'total_price': total_price,
    })


def billing_add(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())

    if request.method == "POST":
        data = request.POST
        qr_image = request.FILES.get('qr_code_image')

        billing = BillingDetail(
            first_name=data['first_name'],
            last_name=data['last_name'],
            country=data['country'],
            address=data['address'],
            town=data['town'],
            postcode=data['postcode'],
            phone=data['phone'],
            email=data['email'],
            qr_code_image=qr_image,
            total=data['total']
        )
        billing.save()
        return redirect('billing_list')
    
    return render(request, 'electro/checkout.html', {
        'cart': cart,
        'total_price': total_price,
    })

def billing_list(request):
    billings = BillingDetail.objects.all()
    return render(request, 'electro/BillingList.html', {'billings': billings})

