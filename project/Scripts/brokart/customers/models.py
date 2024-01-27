from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))  #This enumeration can be used in various parts of your code to represent these two states.
    name = models.CharField(max_length = 200)
    address = models.TextField()
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name = 'customer')
    phone = models.CharField(max_length = 10)
    delete_status = models.IntegerField(choices = DELETE_CHOICES,default = LIVE)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)
    

    def __str__(self) -> str:
        return self.name