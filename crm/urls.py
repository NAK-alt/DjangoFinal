from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import views from your app (replace 'accounts' with your app name if different)
from accounts import views  

urlpatterns = [
    path('admin/', admin.site.urls),

    # App URLs
    path('', include('accounts.urls')),

    # CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Product and Cart URLs
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout_view'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
