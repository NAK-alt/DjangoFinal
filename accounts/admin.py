from django.contrib import admin
from.models import *
from django.utils.html import format_html


# Register your models here.

admin.site.site_header = "ELECTO"
admin.site.site_title = "Electro Website"
admin.site.index_title = "Electro Website Data"

class ProductAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.productImage:
            return format_html(
                '<img src="/static{}" style="width: 100px; height: auto;" />',
                obj.productImage.url
            )
        return "No Image"

    image_preview.short_description = 'Image Preview'

    list_display = ["image_preview", "productName", "categoryID", "price", "productDate"]
    list_filter = ["productDate"]
    search_fields = ["productName"]
    date_hierarchy = "productDate"
    list_per_page = 3
    readonly_fields = ["image_preview"]


admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(ImageType)
admin.site.register(ProductDetail)
admin.site.register(ProductDetailImage)
admin.site.register(BillingDetail)

