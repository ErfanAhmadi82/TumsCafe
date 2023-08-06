from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, User, Type, Cart, CartItem
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from datetime import datetime


# Create your views here.
@csrf_exempt
def CreateCart(request):
    if request.user.is_authenticated:
        
        if not Cart.objects.filter(user = request.user).exists():
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
    template = loader.get_template("Cart.html")
    return redirect("/")


class HomePage(TemplateView):
    template_name = "HomePage.html"

def AddToCart(request):
   Product.AddToCart(request.user)
    

class Type_View(ListView):
    model = Type
    template_name = "Products.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print("CONTEXT:", context)
    #     return context
    
class Products_View(ListView):
    model = Product
    template_name = "Products.html"

@csrf_exempt
def NewUser(request):
    this_user = request.GET["username"]
    this_password = request.GET["password"]
    this_email = request.GET["email"]
    User.objects.create_user(username = this_user, password = this_password, email = this_email)
    context = {
        "user": "done"
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
    CartItem.objects.create(product=product, cart = Cart.objects.filter(user = request.user).first())

    # deliver product #

    return redirect(reverse("Products"))