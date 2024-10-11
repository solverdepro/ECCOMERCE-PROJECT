from django.shortcuts import render
from product.models import Product

# Create your views here.


def home(request):
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products':products,
    }
    return render(request, 'home.html', context)

def cart(request):
    return render(request, 'cart.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def order_complete(request):
    return render(request,'order_complete.html')

def place_order(request):
    return render(request,'place_order.html')

def product_item(request):
    return render(request,'product_item.html')

def register(request):
    return render(request,'register.html')

def search_result(request):
    return render(request,'search_result.html')

def signin(request):
    return render(request,'signin.html')

# def store(request):
#     return render(request,'store.html')
