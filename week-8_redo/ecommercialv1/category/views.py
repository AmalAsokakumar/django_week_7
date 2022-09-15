from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CategoryForm
from django.contrib import messages
from .models import Categories as Category


# Create your views here.
def add_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('category_success') #if this is valid it will invoke the upload_pic function.
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'form': form})

def upload_pic(request):
    messages.success(request,'Category added successfully ') 
    return redirect('add_category')
    # return HttpResponse('category added successful') 

def view_category(request):
    form = Category.objects.all()
    context ={
        'form': form,
        'title': 'Category View'
    }
    return render(request,'view_category.html', context)



def delete_category(request, id):
    print('\n\n delete category \n\n')
    user=request.user
    if user.is_authenticated:
        Category.objects.filter(pk=id).delete()
        return redirect('category_view')
    else:
        return redirect('category_view')
    
    
def edit_category(request, id):
    print('\n\nEdit category')
    user = request.user
    if user.is_authenticated:
        print('super user authentication completed\n\n')
        category = get_object_or_404(Category, pk=id)
        form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('category_view')
        return render(request, 'edit_category.html', {'form': form})
    return redirect('/') 