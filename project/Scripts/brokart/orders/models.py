from django.db import models
from customers.models  import Customer
from products.models  import Product

# Create your models here.
class Order(models.Model):  # it is used to indicate cart items
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))  #This enumeration can be used in various parts of your code to represent these two states.
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES =( (ORDER_PROCESSED,'ORDER_PROCESSED'),
                     (ORDER_DELIVERED, 'ORDER_DELIVERED'),
                     (ORDER_REJECTED,'ORDER_REJECTED')
                    ) 
   
    order_status = models.IntegerField(choices = STATUS_CHOICES,default = CART_STAGE )
    owner = models.ForeignKey(Customer,on_delete = models.SET_NULL,related_name = 'owner',null = True)
    delete_status = models.IntegerField(choices = DELETE_CHOICES,default = LIVE)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)


class OrderedItem(models.Model):
    product = models.ForeignKey(Product,on_delete = models.SET_NULL,related_name='added_carts',null = True)   
    quantity = models.IntegerField(default = 1)
    owner = models.ForeignKey(Order,on_delete = models.CASCADE,related_name = 'added_items')