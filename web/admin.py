from django.contrib import admin
from .models import Product, Cart, CartItem
# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "cart_price", "cart_objects"]
    readonly_fields = ["cart_objects", "cart_price"]
admin.site.register(Cart,CartAdmin)
