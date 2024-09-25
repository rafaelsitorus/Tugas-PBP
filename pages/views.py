from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')

def home_view(request, *args, **kwargs):
	product_entries = Product.objects.all()

	context = {
		'name' : request.user.username,
		'class': 'PBP F',
        'npm': '2306244923',
		'last_login': request.COOKIES['last_login'],
	}

	return render(request, "home.html", context)