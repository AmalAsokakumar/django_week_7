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






@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def admin_login(request):
    # if 'email' in request.session:
        # return redirect('admin_home')
    
    if request.user.is_authenticated:
         return redirect('/')  # create a templated to handle this 
     
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password, is_superuser=True)
        if user is not None:
            auth.login(request,user)
            # request.session['email']= email
            
            return redirect('admin_home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('admin_login')
    else:
        context={}
        return render(request, 'sneat/admin_login.html',{})    
    




def admin_logout(request):
    auth.logout(request)
    return redirect('admin_login')





@login_required(login_url= 'admin_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def admin_home(request):
    # if 'email' in request.session:
        # return HttpResponse('home view')
    # return render(request, 'sneat/admin_index.html', {}) # for testing temp hide it 
    return render(request, 'admin_index.html', {})
    # else: 
    #     return redirect ('admin_login')
