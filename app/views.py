from itertools import product
from lib2to3.fixes.fix_input import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, CategoryProduct
# Create your views here.
def home_page(request):
    try:
        if request.user.is_authenticated():
            products = Product.objects.all()
            categories = CategoryProduct.objects.all()
            context = {
                'products':products,
                'categories':categories
            }
            return render(request,'home.html', context)
        else:
            return redirect('about')
    except:
        return redirect('about')

def about(request):
    try:
        if request.user.is_authenticated():
            return redirect('home.html')
        else:
            return render(request, 'about.html')
    except:
        return render(request, 'about.html')

def categories_page(request, pk):
    categories = CategoryProduct.objects.get(id=pk)
    products = Product.objects.filter(pr_category=categories)
    context = {
        'products':products
    }
    return render(request, 'categories.html', context)