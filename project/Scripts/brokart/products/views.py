from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request,'home.html')

def list_products(request):
    product_list = Product.objects.all()
    context = {'products':product_list}
    return render(request,'product_details.html',context)


def detail_product(request):
    return render(request,'product_description_layout.html')

