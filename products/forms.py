from django import forms
from django.forms import ModelForm
from products.models import Product
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name", 
            "price",
            "quantity"
        ]
    
    def clean_product(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)