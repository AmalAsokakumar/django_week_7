from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Product
from category.models import Categories as category
from brand.models import Brands as brand
from .forms import ProductForm
# Create your views here.


# for private function in product details 

from cart.views import _cart_id
from cart.models import CartItem

# for paginator function
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  


# for search function
from django.db.models import Q





# def search(request):
#     return HttpResponse('check')
    # if 'keyword' in request.GET:                                                                        # checking for if the request have this 'keyword' 
    #     print('\n\n keyword found \n \n ')
    #     keyword = request.GET['keyword']                                                                #if > store the value of the keyword variable is stored in > keyword 
    #     if keyword :                                                                                    # we are only doing these operation if the keyword is not empty.
    #         print('\n\n print the search key word' + str(keyword))
    #         products = Product.objects.order_by('-created_date').filter(description__icontains=keyword) # here description < is a field in Product model and "__icontains" is a function which looks inside the description for a match with the search
    #     context = {
    #             'products': products,
    #            }
    #     return render(request, 'user/shop.html', context)
    # return render(request, 'user/shop.html')
    





def store(request, category_slug = None ):                                                           # we are passing a slug field to filter the content based on the user request 
    categories = None
    products = None
    if category_slug != None:                                                                       # if the slug is not none, we have to do some database operations.
        categories = get_object_or_404(category, slug=category_slug)                                # what this query set will do is like it will look for a the requested objects if not found it will show us a 404 error. (,in category models slug field )
        products = Product.objects.filter(category=categories, is_available=True)                   # to get all the product in the categories if it's available.
                                                                                                    # these three lines of codes are repeated.
        paginator = Paginator(products,6)                                                           # product is the model object that we wanted to print, (model_object, number_of_product) is the number of product that we wanted to show.
        page =request.GET.get('page')                                                               # we will capture the url that comes with the page number ('page') < which we enter to navigate like slug
        paged_products = paginator.get_page(page) 
        product_count=products.count()                                                              # to count the products in the category that we have chosen.
    else:                                                                                           # if slug field is empty that is we haven't chosen a category 
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,6)                                                           # product is the model object that we wanted to print, (model_object, number_of_product) is the number of product that we wanted to show.
        page =request.GET.get('page')                                                               # we will capture the url that comes with the page number ('page') < which we enter to navigate like slug
        paged_products = paginator.get_page(page)                                                   # now we have 6 products stored in this page because of "paginator = Paginator(products,6) " function.
        product_count = products.count()                                                            # we are finding product count using python function. 
    
    context = {
        'products':paged_products,                                                                  #
         #'products': products,                                                                     # we use paginator to customize the number of product that we wanted to show 
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
        single_product = Product.objects.get(category__slug = category_slug, slug= product_slug)                    # here we wanted to get a hold of the slug of the category which is present in the category app. (__slug is a method to access the slug field of that category = which should be matched against the slug field in the url request)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product= single_product).exists()        #  __cart to check the cart model ('cart'  < __cart_id ), because cart is a foreign key of cart item. so first we are accessing the cart first then through it we are accessing ' cart_id' < so that is the reason we are using the under score. '_cart_id(request) is the private function we created inside the cart view function. then it is filter by single product.
                                                                                                                # return HttpResponse(in_cart)   # if the above query returns anything, it will be true  then we are not gonna show an add button.
                                                                                                                # exit() # if the above condition is true it will simply exit the code.
    except Exception as e:
         raise e
    context={
        'single_product': single_product,                                                           # creating a context dictionary.
        'in_cart'       : in_cart,                                                                  # check result of the  item is already in cart or not.
     }
    return render(request, 'user/shop_single.html', context)










def search(request):
    products= None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter( Q(description__icontains=keyword) | Q(product_name__icontains=keyword)) # "filter(description__icontains=keyword , product_name__icontains=keyword , brand_name__icontains=keyword)"in the filter section we can use & and , for and operations and 'Q' - or query set for or operations 
            # products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'user/shop.html', context)











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


