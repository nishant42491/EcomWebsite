from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Products
class ProductListView(ListView):
    model = Products
    template_name = 'products.html'

class ProductDetailView(DetailView):
    model = Products
    template_name= 'productsdetail.html'

