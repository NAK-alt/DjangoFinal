from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Product, Category, ProductDetail, ProductDetailImage, BillingDetail
from django.templatetags.static import static
from django.http import HttpResponse
import random
import os

# ----------------- Simple pages -----------------
def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def blank(request):
    return render(request, 'electro/blank.html')

def product(request):
    return render(request, 'electro/product.html')

def store(request):
    return render(request, 'electro/store.html')

def HotDeal(request):
    return render(request, 'electro/HotDeal.html')

def Categories(request):
    return render(request, 'electro/categories.html')

def checkout(request):
    return render(request, 'electro/checkout.html')
def Blog(request):
    return render(request, 'electro/Blog.html')


# ----------------- Index / Listing pages -----------------
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
    selected_category = request.GET.get('category')
    ObjDTproduct = Product.objects.filter(categoryID=selected_category) if selected_category else Product.objects.all()

    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': ObjDTCategory,
    }
    return render(request, 'electro/All.html', context)


def laptop(request):
    return _category_filter(request, 'Laptop', 'electro/laptop.html')

def smartphone(request):
    return _category_filter(request, 'smartphone', 'electro/smartphone.html')

def cameras(request):
    return _category_filter(request, 'camera', 'electro/cameras.html')

def accessories(request):
    return _category_filter(request, 'accessories', 'electro/accessories.html')


def _category_filter(request, category_name, template_name):
    ObjDTCategory = Category.objects.all()
    ObjDTproduct = Product.objects.filter(categoryID__categoryName__iexact=category_name)
    context = {
        'ObjDTproduct': ObjDTproduct,
        'ObjDTCategory': ObjDTCategory,
    }
    return render(request, template_name, context)


# ----------------- Product Detail -----------------
def productDetail(request, pk):
    ObjDTCategory = Category.objects.all()
    ObjDTProductDetail = get_object_or_404(Product, id=pk)
    ObjDTProductDetailInfo = ProductDetail.objects.filter(productID=ObjDTProductDetail).first()
    ObjDTProductDetailImage = ProductDetailImage.objects.filter(productID=ObjDTProductDetail)

    related_products = Product.objects.filter(categoryID=ObjDTProductDetail.categoryID).exclude(id=pk)[:4]

    category_template_map = {
        1: 'electro/productSectionSmartphone.html',
        2: 'electro/productSectionlaptop.html',
        3: 'electro/productSectionCamera.html',
        4: 'electro/productSectionAccessories.html',
    }

    dynamic_template = category_template_map.get(
        ObjDTProductDetail.categoryID.id,
        'electro/productSection.html'
    )

    context = {
        'ObjDTCategory': ObjDTCategory,
        'ObjDTProductDetail': ObjDTProductDetail,
        'ObjDTProductDetailInfo': ObjDTProductDetailInfo,
        'ObjDTProductDetailImage': ObjDTProductDetailImage,
        'related_products': related_products,
        'dynamic_template': dynamic_template,
    }

    return render(request, 'electro/productDetail.html', context)


# ----------------- Cart Functions -----------------
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Product, id=product_id)

    # Use the filename from the database, but assume it lives in static/images/Products/
    if product.productImage:
        # This gets just 'filename.jpg' regardless of how it was uploaded
        filename = os.path.basename(product.productImage.name)
        image_path = f"images/Products/{filename}"
    else:
        image_path = "images/no-image.png"

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
        cart[str(product_id)]['total'] = cart[str(product_id)]['quantity'] * cart[str(product_id)]['price']
    else:
        cart[str(product_id)] = {
            'productName': product.productName,
            'price': float(product.price),
            'quantity': quantity,
            'image': image_path, # Storing "images/Products/filename.jpg"
            'total': float(product.price) * quantity
        }

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('view_cart')
def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())
    return render(request, 'electro/shoping-cart.html', {
        'cart': cart,
        'total_price': total_price
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('view_cart')


def checkout_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())
    return render(request, 'electro/checkout.html', {
        'cart': cart,
        'total_price': total_price,
    })


# ----------------- Billing -----------------
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
