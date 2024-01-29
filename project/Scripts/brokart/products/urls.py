from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.home,name='home'),
    path('product_list/', views.list_products,name='list_products'),
    path('product_details/', views.detail_product,name='detail_product'),
    

    
] 