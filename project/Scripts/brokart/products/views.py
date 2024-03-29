from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
import random

# Create your views here.
def home(request):
    featured_product = Product.objects.order_by('priority')[:4]
    latest_product = Product.objects.order_by('-id')[:4]
    random_objects = Product.objects.order_by('?')[:3]  #to select any 3 random objects
    context = {'featured_product':featured_product,
               'latest_product':latest_product,
               'rand_obj':random_objects
               }
    return render(request,'home.html',context)

def list_products(request):
    page = 1
    if  request.GET:
        page = request.GET.get('page',1)

    product_list = Product.objects.order_by('-priority')
    product_paginator = Paginator(product_list,3)
    product_list = product_paginator.get_page(page)
    context = {'products':product_list}
    return render(request,'product_details.html',context)


def detail_product(request,pk):
    list = []
    product = Product.objects.get(pk=pk)
    
    
   # for related products
    random_objects = Product.objects.order_by('?')[:4]  #this is used to select 4 random objects from Product table
    
    context = {'product':product,
               'related_products':random_objects
               }
      
    return render(request,'product_description_layout.html',context)



