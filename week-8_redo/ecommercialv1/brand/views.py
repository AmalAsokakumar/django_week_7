from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *  

def add_brand(request):
    
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BrandForm()
        return render(request,'brand.html',{form:form})
    
def upload_pic(request):
    return HttpResponse('Brand added successfully ')