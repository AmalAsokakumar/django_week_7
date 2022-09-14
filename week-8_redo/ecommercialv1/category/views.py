from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CategoryForm
from django.contrib import messages
from .models import category


# Create your views here.
def add_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('success') #if this is valid it will invoke the upload_pic function.
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'form': form})

def upload_pic(request):
    messages.success(request,'Category added successfully ') 
    return redirect('add_category')
    # return HttpResponse('category added successful') 

def view_category(request):
    form = category.objects.all()
    context ={
        'form': form,
        'title': 'Category View'
    }
    return render(request,'view_category.html', context)