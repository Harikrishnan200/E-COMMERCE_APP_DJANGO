from . import views
from .views import index
from django.urls import path,include

urlpatterns = [
    path('', views.index,name='home'),
    path('product_list/', views.list_products,name='list_products'),
    

    
] 