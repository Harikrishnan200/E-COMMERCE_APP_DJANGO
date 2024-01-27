from django.db import models

# models for product
class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))  #This enumeration can be used in various parts of your code to represent these two states.
    title = models.CharField(max_length = 200)
    price = models.FloatField()
    description = models.TextField()
    images = models.ImageField(upload_to='/media')
    priority = models.IntegerField() # used to set the priority of that product
    delete_status = models.IntegerField(choices = DELETE_CHOICES,default = LIVE)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)


    def __str__(self) -> str:
        return self.title


