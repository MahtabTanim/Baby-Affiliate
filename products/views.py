from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'name':'Baby Affiliate',
        'products':products
    }
    return render(request,'product_list.html',context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'name':'Baby Affiliate',
        'products':products
    }
    return render(request,'product_list.html',context)

def products(request,id=None):
    products = Product.objects.all() 
    try:
        product = products[id-1]
        name = product.name
    except :
        product = None
        name = 'Not found'
    context = {
        'name' : name,
        'product' : product
    }
    return render(request,'product_detail.html',context)
