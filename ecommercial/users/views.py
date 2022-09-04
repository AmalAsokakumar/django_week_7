from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'user/index.html',{})
def shop(request):
    return render(request, 'user/shop.html',{})
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