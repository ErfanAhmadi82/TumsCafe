from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
# from . import views
# Create your models here.

class Type(models.Model):
     Name = models.CharField(max_length=255,)
     def __str__(self) -> str:
        return self.Name
     def type_objects(self):
          type_objects_list = list()
          for type_object in Product.objects.filter(Type=self):
               type_objects_list.append(type_object)
          return type_objects_list

class Product(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.BigIntegerField()
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="media", max_length=100, height_field=None, width_field=None)
    def __str__(self) -> str:
        return self.Name
    def AddToCart(self, this_user):
         CartItem.objects.create(product=self, cart = Cart.objects.filter(user = this_user))
    
    # def get_absolute_url(self):
    #      return reverse("post_detail", kwargs={"pk": self.pk})

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    def cart_price(self):
            price = 0
            for cart_item in CartItem.objects.filter(cart=self):
                price += cart_item.item_over_all_price()
            return price
    def cart_objects(self):
         cart_objects_list = list()
         for cart_item in CartItem.objects.filter(cart=self):
              cart_objects_list.append(cart_item)
         return cart_objects_list
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    # ItemOverAllPrice = item.product.Price * quantity
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.product.Name + "*" + str(self.quantity)
    def item_over_all_price(self):
        return self.product.Price * self.quantity
    