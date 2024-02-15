from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from products.models import Product
from django.contrib import messages
# Create your views here.

def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )
    context = {'cart':cart_obj}
    return render(request,'cart.html',context)   



def add_to_cart(request):
    if request.POST:
        user = request.user 
        customer = user.customer_profile    #customer object is fetched through reverse relationship
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj,created = Order.objects.get_or_create(  #here create an object of customer table with some conditions specified below
            owner = customer,
            order_status = Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id) 
        ordered_item,created = OrderedItem.objects.get_or_create(  #here create an object of table OrderedItems with some conditions specified below
            product = product,   #inside the get_or_create fn we assign objects of each field not id or other
            owner = cart_obj,
        )
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity = ordered_item.quantity + quantity
            ordered_item.save()
        return redirect('cart') 
    
def remove_item_from_cart(request,pk):
    item = OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')
    
def checkout_cart(request):
    try:
        if request.POST:
            user = request.user 
            customer = user.customer_profile    #customer object is fetched through reverse relationship
            quantity = int(request.POST.get('quantity'))
            product_id = request.POST.get('product_id')
            order_obj = Order.objects.get(  #here create an object of customer table with some conditions specified below
                owner = customer,
                order_status = Order.CART_STAGE
            ) 
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.save()       
                status_message = "Your order is processed."
                messages.success(request,status_message)
            else:
                status_message="No items in your cart"  
                messages.error(request,status_message)            
    except Exception as e:
        status_message="Something went wrong" 
        messages.warning(request,str(e))
    return redirect('cart')    
