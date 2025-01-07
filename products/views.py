from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'name':'Baby Affiliate',
        'products':products
    }
    return render(request,'home.html',context)

def products(request):
    products = Product.objects.all()
    context = {
        'name':'Baby Affiliate',
        'products':products
    }
    return render(request,'home.html',context)
