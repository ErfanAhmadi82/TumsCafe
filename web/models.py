from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# from . import views
# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.BigIntegerField(max_length=255)
    photo = models.ImageField(upload_to="media", max_length=100, height_field=None, width_field=None)
    def __str__(self) -> str:
        return self.Name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # ItemOverAllPrice = product * quantity
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.product.Name + "*" + str(self.quantity)
