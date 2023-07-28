from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
# Create your views here.

class HomePage(TemplateView):
    template_name = "HomePage.html"

class Products_View(ListView):
    model = Product
    template_name = "Products.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print("CONTEXT:", context)
    #     return context
    
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