from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.

def home_view(request, *args, **kwargs):
	product_entries = Product.objects.all()
	return render(request, "home.html", {})