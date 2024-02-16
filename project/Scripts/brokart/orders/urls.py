from . import views
from django.urls import path,include

urlpatterns = [
    path('cart/', views.show_cart,name='cart'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove_item_from_cart/<pk>',views.remove_item_from_cart,name='remove_item_from_cart'),
    path('checkout/',views.checkout_cart,name='checkout'),
    path('show_orders/', views.show_orders,name='orders'),
    
    

    
] 