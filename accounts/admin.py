from django.contrib import admin
from.models import *

# Register your models here.

admin.site.site_header = "ELECTO"
admin.site.site_title = "Electro Website"
admin.site.index_title = "Electro Website Data"



admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductDetailImage)

