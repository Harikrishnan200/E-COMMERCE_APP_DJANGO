from django.db import models
from customers.models  import Customer
from products.models  import Product

# Create your models here.
class Order(models.Model):  # it is used to indicate cart items
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))  #This enumeration can be used in various parts of your code to represent these two states.
    owner = models.ForeignKey(Customer,on_delete = models.CASCADE,related_name = 'owner')
    delete_status = models.IntegerField(choices = DELETE_CHOICES,default = LIVE)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)


class OrderedItem(models.Model):
    product = models.ForeignKey(Product,related_name = 'added_cart', no_delete = models.SET_NULL)   
    quantity = models.IntegerField(default = 1)
 #   owner = models.ForeignKey(Order,on_delete = models.CASCADE,related_name = 'added_items')