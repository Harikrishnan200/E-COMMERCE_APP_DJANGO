from django.shortcuts import render,redirect
from .models import Order,OrderedItem
# Create your views here.

def show_cart(request):
    return render(request,'cart.html')   



def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile #customer object is fetched through reverse relationship
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj,created = Order.objects.get_or_create(  #here create an object of customer table with some conditions specified below
            owner = customer,
            order_status = Order.CART_STAGE
        )
        ordered_item = OrderedItem.objects.create(  #here create an object of table OrderedItems with some conditions specified below
            product = product_id,  
            owner = cart_obj,
            quantity = quantity
        )
        return redirect('cart')