from . import views
from django.urls import path,include

urlpatterns = [
    path('cart/', views.cart,name='cart'),
    
    

    
] 