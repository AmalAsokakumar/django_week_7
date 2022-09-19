from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth










# register function  with out any otp method for activation. need more adjustments 
def register(request):
    
    if request.method == 'POST':
            
        
        form = RegistrationForm(request.POST)                                                               # here the request.post will contain all the field values from the form submission. 
        
        if form.is_valid():                                                                                 # to check whether all the field in this form is valid or not. 
            print( ' \n \n for is validated ')
            first_name      = form.cleaned_data['first_name']                                                    # while using django forms we use cleaned_data to fetch the values/from request
            last_name       = form.cleaned_data['last_name']
            email           = form.cleaned_data['email']
            phone_number    = form.cleaned_data['phone_number']
            password        = form.cleaned_data['password']                                                        # we will validate the conform password with password in form level only. 
            # auto generate username
            username        = email.split('@')[0]                                                                  # here we are using first part of email to create a username for the user. 
                                                                                                            # to create a user,
                                                                                                            # here the create_user is from django  models we have create_user in MyAccountManager, similarly there is a function to create a super user also.
            user_1 = Account.objects.create_user(first_name=first_name,                                       # here we are using the create user function that we created in account_ Models.
                                               last_name=last_name,
                                               email=email,
                                               username=username,
                                               password=password,
                                               
                                               )                                                            # there is no field to accept phone number in models.py so we are attaching it like this.
            user_1.phone_number = phone_number                                                                # this will update the user object with the phone number. because we hav
            user_1.save()                                                                                     # this field will be created in the database. 
            messages.success(request, 'registration success')
            return redirect('register')
    else:       
        form = RegistrationForm()
    context = {
            'form': form, 
    }
    return render (request,'sneat/auth-register-basic.html', context)

    
    
# # Create your views here.
# def register(request):
#     form = RegistrationForm()
#     context = {'form': form}
#     # return render(request, 'sneat/auth-register-basic.html', context)
#     return render(request, 'register.html', context)




# basic views 
def home(request):
    return render(request, 'user/index.html',{})
def contact(request):
    return render(request, 'user/contact.html',{})
def about(request):
    return render(request, 'user/about.html',{})





#user 
def login(request):
    if request.method == 'POST':
        email       = request.POST['email']
        password    = request.POST['password']
        
        user_1 = auth.authenticate(email=email, password=password)
        if user_1 is not None:
            auth.login(request, user_1)
            # messages.success(request,'you have successfully logged in')
            return redirect('user_home')  # should be redirect to dashboard
        else:
            messages.error(request, 'invalid credentials ')
            return redirect('login')
            
    return render(request, 'login.html', {})
def logout(request):
    pass