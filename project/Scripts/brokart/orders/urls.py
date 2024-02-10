from . import views
from django.urls import path,include

urlpatterns = [
    path('cart/', views.show_cart,name='cart'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    
    

    
] 