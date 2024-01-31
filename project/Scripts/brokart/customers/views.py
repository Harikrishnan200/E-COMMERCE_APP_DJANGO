from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def account(request):

    if request.POST and 'register' in request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            # create user account
            user = User.objects.create_user(username=username,password=password ,email=email)
            return redirect('home')
        
        except Exception as e:
            error_message = "invalid username or invalid creditials"
            messages.error(request,error_message)
    return render(request,'account.html')