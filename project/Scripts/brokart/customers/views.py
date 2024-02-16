from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as userLogout
from django.contrib import messages
from . models import Customer
# Create your views here.

def logout(request):
    userLogout(request)
    return redirect('account')
def account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            # create user account
            user = User.objects.create_user(username=username,
                                            password=password ,
                                            email=email
                                        )
            #create customer account
            customer = Customer.objects.create(
                name = username,
                user = user,
                address = address,
                phone = phone
              
            )
            

            success_message = 'Registered successfully'
            messages.success(request,success_message)
        
        except Exception as e:
            error_message = "Error!!  invalid username or invalid creditials"
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate( username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            messages.error(request,error_message)
    return render(request,'account.html',context)