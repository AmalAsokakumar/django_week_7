from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BrandForm
from django.contrib import messages 
from . models import Brands as Brand


def add_brand(request):
    
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('brand_success')
    else:
        form = BrandForm()
        return render(request,'brand.html',{'form':form})
    
def upload_pic(request):
    messages.success(request,'Brand added successfully ') 
    return redirect('add_brand')





def view_brand(request):
    print('\n \ninside brand view fn  \n\n')
    form = Brand.objects.all()
    context= {
        'form': form,
        'title':'Brand View'
    }
    return render(request,'view_brand.html',context)
    





def delete_brand(request, id):
    print('\n \n deleting brand \n\n')
    user= request.user
    if user.is_authenticated:
        Brand.objects.filter(pk=id).delete()
        return redirect('brand_view')
    else:
        return redirect('brand_view')    # should be replaced to login in view 
    
    
    
    
def edit_brand(request, id):
    print('\n\n edit_ brand \n')
    user = request.user
    if user.is_superuser:
        print('super user authentication completed  \n\n')
        brand = get_object_or_404(Brand, pk=id) # to prepopulated the form 
        # brand = Brand.objects.get(pk=id) # getting details of the object from models using primary key 
        form = BrandForm(request.POST or None, request.FILES or None, instance=brand)
        if form.is_valid():
            print("form is valid ")
            # form.save() # saving the changes.
            edit = form.save(commit=False)# in order to add this condition i disable the above condition.
            edit.save() #
            return redirect('brand_view')
        return render(request, 'edit_brand.html', {'form': form, 'type':'Brand '} )
    return redirect('/') # un authentication users will be redirected to default page {{ need to change this field }}
    # return render(request,'edit_brand.html')
    