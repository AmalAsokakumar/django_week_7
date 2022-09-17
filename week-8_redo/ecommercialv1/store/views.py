from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Product
from category.models import Categories as category
from brand.models import Brands as brand
from .forms import ProductForm
# Create your views here.


def store(request, category_slug = None ): # we are passing a slug field to filter the content based on the user request 
    categories = None
    products = None
    if category_slug != None: # if the slug is not none, we have to do some database operations.
        categories = get_object_or_404(category, slug=category_slug)# what this query set will do is like it will look for a the requested objects if not found it will show us a 404 error. (,in category models slug field )
        products = Product.objects.filter(category=categories, is_available=True)# to get all the product in the categories if it's available.
        product_count=products.count()# to count the products in the category that we have chosen.
    else: # if slug field is empty that is we haven't chosen a category 
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()# we are finding product count using python function. 
    
    context = {
        
        'products': products,
        'product_count': product_count,
        
    }
    return render(request,'user/shop.html',context)







# def store(request, brand_slug = None ): # we are passing a slug field to filter the content based on the user request 
#     brands = None
#     product_s = None
#     if brand_slug != None: # if the slug is not none, we have to do some database operations.
#         brands = get_object_or_404(brand, slug=brand_slug)# what this query set will do is like it will look for a the requested objects if not found it will show us a 404 error. (,in category models slug field )
#         products = Product.objects.filter(brand=brands, is_available=True)# to get all the product in the categories if it's available.
#         product_count=products.count()# to count the products in the category that we have chosen.
#     else: # if slug field is empty that is we haven't chosen a category 
#         products = Product.objects.all().filter(is_available=True)
#         product_count = products.count()# we are finding product count using python function. 
    
#     context = {
        
#         'products': products,
#         'product_count': product_count,
        
#     }
#     return render(request,'user/shop.html',context)








def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug= product_slug) # here we wanted to get a hold of the slug of the category which is present in the category app. (__slug is a method to access the slug field of that category = which should be matched against the slug field in the url request)
    except Exception as e:
         raise e
    context={
        'single_product': single_product,  # creating a context dictionary.
     }
    return render(request, 'user/shop_single.html', context)




































# Create your views here.
def add_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('product_success') #if this is valid it will invoke the upload_pic function.
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form})

def upload_pic(request):
    messages.success(request,'Product added successfully ') 
    return redirect('add_product')





def view_product(request):
    form = Product.objects.all()
    context ={
        'form': form,
        'title': 'Product View'
    }
    return render(request,'view_Product.html', context)




def delete_product(request, id):
    print('\n\n delete product \n\n')
    user=request.user
    if user.is_authenticated:
        Product.objects.filter(pk=id).delete()
        return redirect('product_view')
    else:
        return redirect('/')
    


    
def edit_product(request, id):
    print('\n\nEdit product')
    user = request.user
    if user.is_authenticated:
        print('super user authentication completed\n\n')
        product = get_object_or_404(Product, pk=id)
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('product_view')
        return render(request, 'editCB.html', {'form': form})
    return redirect('/') 