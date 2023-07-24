from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product
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
    
