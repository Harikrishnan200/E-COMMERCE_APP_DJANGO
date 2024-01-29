from . import views
from django.urls import path,include

urlpatterns = [
    path('account/', views.account,name='account'),
    
    

    
] 