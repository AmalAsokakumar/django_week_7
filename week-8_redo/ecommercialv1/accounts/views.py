from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control


# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



# Create your views here.


# my questions are like what are the fields that these default django form have and how do i know them ?



# register function  with out any otp method for activation. need more adjustments 
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)                                                                       # here the request.post will contain all the field values from the form submission. 

        if form.is_valid():                                                                                                 # to check whether all the field in this form is valid or not. 
            first_name = form.cleaned_data['first_name']                                                                # while using django forms we use cleaned_data to fetch the values/from request
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']                                                             # we will validate the conform password with password in form level only. 
            username = email.split('@')[0]                                                                              # here we are using first part of email to create a username for the user. 
                                                                                                            # to create a user,
                                                                                                # here the create_user is from django  models we have create_user in MyAccountManager, similarly there is a function to create a super user also.
            user = Account.objects.create_user(first_name=first_name,
                                               last_name=last_name,
                                               email=email,
                                               password=password,
                                               username=username
                                               ) # there is no field to accept phone number in models.py so we are attaching it like.
            user.phone_number = phone_number # this will update the user object with the phone number.
            user.save() # this field will be created in the database. 
            return render (request, 'login.html',{}) 
            
    else:       
            form = RegistrationForm()
    context = {
            'form': form, 
        }
    return render (request, 'register.html', context)










def admin_list_users(request): # need to recheck this 
    #list= Account.objects.order_by('id')
    list= Account.objects.filter( is_superuser=False).order_by('id')
    
    context = {
        'list': list,
    }
    return render(request, 'list_users.html',context)



def admin_user_enable(request, id):
    user = Account.objects.get(id = id)
    user.is_active = True
    user.save()
    return redirect('admin_list_users')

def admin_user_block(request, id):
    user = Account.objects.get(id = id)
    user.is_active = False
    user.save()
    return redirect('admin_list_users')
   

    


    
    






#admin 
#authentication steps are not added. 


@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def admin_login(request):
    # if 'email' in request.session:
        # return redirect('admin_home')
    
    if request.user.is_authenticated:
         return redirect('admin_home')  # create a templated to handle this 
     
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            # request.session['email']= email
            
            return redirect('admin_home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('admin_login')
    else:
        context={}
        return render(request, 'login.html',{})    
    



@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def login(request):
    # if 'email' in request.session:
        # return redirect('admin_home')
    
    if request.user.is_authenticated:
         return redirect('/')  # create a templated to handle this 
     
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            # request.session['email']= email
            
            return redirect('/')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('/')
    else:
        context={}
    return render(request, 'login.html',{})   





@login_required(login_url = 'login')
def admin_logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out')
    return redirect('admin_login')




@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out')
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



# basic views 
def home(request):
    return render(request, 'user/index.html',{})
def contact(request):
    return render(request, 'user/contact.html',{})
def about(request):
    return render(request, 'user/about.html',{})



