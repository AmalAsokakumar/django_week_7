from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import category
# Create your views here.

def store(request, category_slug = None ): # we are passing a slug field to filter the content based on the user request 
    categories = None
    products = None
    if category_slug != None: # if the slug is not none, we have to do some database operations.
        categories = get_object_or_404(category, slug=category_slug)# what this query set will do is like it will look for a the requested objects if not found it will show us a 404 error. (,in category models slug field )
        products =Product.objects.filter(category=categories, is_available=True)# to get all the product in the categories if it's available.
        product_count=products.count()# to count the products in the category that we have chosen.
    else: # if slug field is empty that is we haven't chosen a category 
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()# we are finding product count using python function. 
    
    context = {
        
        'products': products,
        'product_count': product_count,
        
    }
    return render(request,'user/shop.html',context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug= product_slug) # here we wanted to get a hold of the slug of the category which is present in the category app. (__slug is a method to access the slug field of that category = which should be matched against the slug field in the url request)
    except Exception as e:
        raise e
    context={
        'single_product': single_product,  # creating a context dictionary.
    }
    return render(request, 'user/shop_single.html', context)