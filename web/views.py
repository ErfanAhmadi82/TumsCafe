from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, User, Type, Cart, CartItem, Order
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from datetime import datetime


# Create your views here.
@csrf_exempt
def CreateCart(request):
    if request.user.is_authenticated:
        
        if not Cart.objects.filter(user = request.user, active = True).exists():
            Cart.objects.create(user = request.user)
            context = {
            "user" : "hello",
        }
        else:
            context = {
            "user" : "how are you",
        }
    else:
        context = {
            "user" : "Please login first"
        }
    return redirect("/")


class HomePage(TemplateView):
    template_name = "HomePage.html"

def AddToCart(request):
   Product.AddToCart(request.user)
    

class Type_View(ListView):
    model = Type
    template_name = "Products.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = CartItem.objects.filter(cart = Cart.objects.filter(user = self.request.user, active = True).first())
        context["price"] = Cart.objects.get(user = self.request.user, active = True).cart_price()
        print("CONTEXT:", context)
        return context
    
class Products_View(ListView):
    model = Product
    template_name = "Products.html"
    # price = Cart.objects.get(user = request.user, active = True).cart_price()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["price"] = Cart.objects.get(user = self.request.user, active = True).cart_price()
        print("CONTEXT:", context)
        return context
    

@csrf_exempt
def NewUser(request):
    this_user = request.GET["username"]
    this_password = request.GET["password"]
    this_email = request.GET["email"]
    User.objects.create_user(username = this_user, password = this_password, email = this_email)
    context = {
        "user": "done",
        "price": Cart.objects.get(user = self.request.user, active = True).cart_price()
    }
    template = loader.get_template("User_Created.html")
    return HttpResponse(template.render(context, request))

            
# class Product_detail(DetailView):
#     model= Product
#     template_name = "Products.html"
#     def add(request, pk):
#         print("hello world")
#         Product.AddToCart(self=Product.objects.filter(pk = Product_detail.pk_url_kwarg), this_user=request.user)  
#         return redirect("/")
    
def order(request, Product_id):
    product = Product.objects.get(id=Product_id)
    if not CartItem.objects.filter(product = Product.objects.filter(id = Product_id).first(), cart = Cart.objects.filter(user = request.user, active = True).first()).exists():
        print("a")        
        CartItem.objects.create(product=product, cart = Cart.objects.filter(user = request.user, active = True).first())

    else:
        print("B")
        num = CartItem.objects.filter(product = Product.objects.filter(id=Product_id).first(), cart = Cart.objects.filter(user = request.user, active = True).first()).first().quantity
        CartItem.objects.filter(product = Product.objects.filter(id=Product_id).first(), cart = Cart.objects.filter(user = request.user, active = True).first()).update(quantity = num + 1)
    # deliver product #

    return redirect(reverse("Products"))

def CartObjects(request):
    items = CartItem.objects.filter(cart = Cart.objects.filter(user = request.user).first())
    template = loader.get_template("Products.html")
    context = {
        "items": items
    }
    return HttpResponse(template.render(context, request))

def NewOrder(request):
    Cart.objects.filter(user = request.user, active = True).update(active = False)
    Cart.objects.create(user = request.user)
    Order.objects.create(cart = Cart.objects.filter(user = request.user, active = False).first())
    return redirect("/")

def DeleteCartItem(request, CartItem_id):
    CartItem.objects.get(id = CartItem_id).delete()
    return redirect(reverse("Products"))

def GetPrice(request):
    price = Cart.objects.get(user = request.user, active = True).cart_price()
    
