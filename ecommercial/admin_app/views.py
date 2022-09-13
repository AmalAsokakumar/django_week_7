from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def admin_login(request):
    # if 'email' in request.session:
        #return redirect('admin_home')
    
    if request.user.is_authenticated:
         return redirect('/')  # create a templated to handle this 
     
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            request.session['email']= email
            
            return redirect('admin_home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('admin_login')
    else:
        context={}
        return render(request, 'sneat/admin_login.html',{})    




def admin_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required(login_url= '/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def admin_home(request):
    # if 'email' in request.session:
        # return HttpResponse('home view')
    return render(request, 'sneat/admin_index.html', {})
    # else: 
    #     return redirect ('admin_login')

