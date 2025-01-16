from django.contrib import admin
from product.models import Product

# Register your models here.
class AddProduct(admin.ModelAdmin):
    list_display = ('productName','description','price','status')

admin.site.register(Product,AddProduct)