from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



# Create your views here.


# my questions are like what are the fields that these default django form have and how do i know them ?




# register function  with out any otp method for activation.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST) # here the request.post will contain all the field values from the form submission. 

        if form.is_valid(): # to check whether all the field in this form is valid or not. 
            first_name = form.cleaned_data['first_name'] # while using django forms we use cleaned_data to fetch the values/from request
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password'] # we will validate the conform password with password in form level only. 
            username = email.split('@')[0] # here we are using first part of email to create a username for the user. 
            # to create a user,
            # here the create_user is from django  models we have create_user in MyAccountManager, similarly there is a function to create a super user also.
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username) # there is no field to accept phone number in models.py so we are attaching it like.
            user.phone_number = phone_number # this will update the user object with the phone number.
            user.save() # this field will be created in the database. 
            return render (request, 'sneat/auth-register-basic.html',{}) 
            
    else:       
        form = RegistrationForm()
        context = {
            'form': form, 
        }
        return render (request, 'sneat/auth-register-basic.html', context)


#login function
def login(request):
    return render(request, 'sneat/auth-login-basic.html', {})

def logout(request):
    pass