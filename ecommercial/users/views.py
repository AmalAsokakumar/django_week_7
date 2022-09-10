from django.shortcuts import render
from store.models import Product

# Create your views here.
def home(request):
    return render(request, 'user/index.html',{})


# def shop(request): # we planned to change its location. 
#     products = Product.objects.all().filter(is_available=True)
    
#     context = {                        # here we are passing the data inside a context dictionary 
#         'products': products,
#     }
    
#     return render(request, 'user/shop.html', context)




def contact(request):
    return render(request, 'user/contact.html',{})
def about(request):
    return render(request, 'user/about.html',{})

def forget_password(request):
     return render(request, 'sneat/auth-forgot-password-basic.html',{})
def login(request):
     return render(request, 'sneat/auth-login-basic.html',{})
def register(request):
     return render(request, 'sneat/auth-register-basic.html',{})