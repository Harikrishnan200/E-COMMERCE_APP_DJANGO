from . import views
from django.urls import path,include

urlpatterns = [
    path('cart/', views.show_cart,name='cart'),
    
    

    
] 