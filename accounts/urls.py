from django.urls import path

from . import views

urlpatterns = [
    path('no/', views.home),
    path('products/', views.products),
    path('customer/', views.customer),


    path('', views.index, name='index'),
    path('blank/', views.blank, name='blank'),
    path('product/', views.product, name='product'),
    path('productDetail/<int:pk>', views.productDetail, name='productDetail'),
    path('store/', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),
    path('HotDeal/', views.HotDeal ,name='HotDeal'),
    path('Categories/', views.Categories ,name='Categories'),
    path('product/', views.product ,name='product'),
    path('laptop/', views.laptop ,name='laptop'),
    path('cameras/', views.cameras ,name='cameras'),
    path('smartphone/', views.smartphone ,name='smartphone'),
    path('accessories/', views.accessories ,name='accessories'),


    
]