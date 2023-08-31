from django.contrib import admin
from .models import Product, Cart, CartItem, Type, Order, Comment
# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "cart_price", "cart_objects"]
    readonly_fields = ["cart_objects", "cart_price"]
admin.site.register(Cart,CartAdmin)
#FreeCodeCamp
class TypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Type, TypeAdmin)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["cart_objects", "price"]
admin.site.register(Order,OrderAdmin)
admin.site.register(Comment)