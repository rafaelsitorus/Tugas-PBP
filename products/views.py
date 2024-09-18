from django.shortcuts import render, redirect
from products.forms import ProductForm
from products.models import Product
from django.http import HttpResponse
from django.core import serializers

# some_file.py

# Create your views here.

def product_create_view(request):
	form = ProductForm(request.POST or None)

	if form.is_valid() and request.method == "POST":
		form.save()
		return redirect('home_view')

	context = {
		'form' : form
	}
     
	return render(request, "products/product_create.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")