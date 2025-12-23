from django.urls import path

from . import views

urlpatterns = [
    path('no/', views.home),
    path('products/', views.products),
    path('customer/', views.customer),


    path('', views.index, name='index'),
    path('blank/', views.blank, name='blank'),
    path('product/', views.product, name='product'),
    path('store/', views.store, name='store'),
    path('HotDeal/', views.HotDeal ,name='HotDeal'),
    path('All/', views.All,name='All'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('checkout_view/', views.checkout_view, name='checkout_view'),
    # path('ShopingCart/', views.ShopingCart, name='ShopingCart'),
    path('checkout_view/', views.checkout_view, name='checkout_view'),
    path('billing_add/', views.billing_add, name='billing_add'),
    path('billing_list/', views.billing_list, name='billing_list'),

    path('productDetail/<int:pk>', views.productDetail, name='productDetail'),
    path('Categories/', views.Categories ,name='Categories'),
    path('product/', views.product ,name='product'),
    path('laptop/', views.laptop ,name='laptop'),
    path('cameras/', views.cameras ,name='cameras'),
    path('smartphone/', views.smartphone ,name='smartphone'),
    path('accessories/', views.accessories ,name='accessories'),


    
]