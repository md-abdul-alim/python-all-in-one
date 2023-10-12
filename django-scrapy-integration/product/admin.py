from django.contrib import admin
from product.models import Product
# Register your models here.

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', ]