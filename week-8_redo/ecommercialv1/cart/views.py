from curses.ascii import HT
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from store.models import Product
from .models import Cart, CartItem
# Create your views here.

from django.core.exceptions import ObjectDoesNotExist




                                                                # this is a private function to create cart id using a section id 
def _cart_id(request):                                          # this is a private function because we use an _ denote that 
    cart = request.session.session_key
    if not cart:                                                # check if the cart variable is empty if it is we are gonna create a one.
        cart = request.session.create()
                                                                #print(' \n\n new session key is created ')
    return cart                                                 # this function will return the cart id 








def add_cart(request, product_id):
                                                                #print(' \n\n add cart',str(product_id))
                                                                #print (' \n\n inside the cart')
    product     = Product.objects.get(id=product_id)                #get the product 
    try:
                                                                 #print(' \n looking for a cart')
        cart    = Cart.objects.get(cart_id=_cart_id(request))    # here we are adding the section id as cart id. to get that we use a private function.  Get the cart, using the cart_id present in the session
    
    except Cart.DoesNotExist:                                    # if cart not exist, we are gonna create one.
        #                                                        print("\n\n cart does not exist")
        cart    = Cart.objects.create(
            cart_id = _cart_id(request)                                 # we will create a cart id using above private function.
        )
        cart.save()
                                                                        # print("\n\n new  cart created ")
                                                                        # print("\n\n new cart is created")
                                                                        # in a cart we can have a number ot item, which can be obtained by combining the product with cart id to create the cart items.
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)    # cart items are stored inside the cart_item variable, in CartItem model manner. 
        cart_item.quantity += 1                                         # to count the number of items in the cart.
        cart_item.save()                                                # save the cart item to the database
                                                                        #print('\nnew item added to the cart\n\n')
    except CartItem.DoesNotExist:                                       #if cart item is empty.
        cart_item   = CartItem.objects.create(                          # things need to create a new cart are these
            product = product,
            quantity= 1,
            cart     = cart,
        )
        cart_item.save()                                                # save the cart item to the database
                                                                        # print('\n\n items are added to the cart ')
                                                                # return HttpResponse(cart_item.product)
                                                                # exit()
    return redirect('view_cart')                                        #initial cart url in the main project.








def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id= _cart_id(request))
    product = get_object_or_404(Product, id=product_id)                 # Product model, product id 
    cart_item = CartItem.objects.get(product=product, cart=cart)        # looking for these variable in the database 
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect ('view_cart')






def remove_cart_item(request, product_id):
    cart        =   Cart.objects.get(cart_id= _cart_id(request))
    product     =   get_object_or_404(Product, id=product_id)
    cart_item   =   CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('view_cart')





def cart(request, total=0, quantity=0, cart_item=None):
                                                                        # print('we are currently inside the cart page')
                                                                        # return HttpResponse('we are in future cart page')
    try:
        tax=0
        grand_total=0
        cart = Cart.objects.get(cart_id=_cart_id(request))              # calling the above private function for the cart id.
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total +=(cart_item.product.price * cart_item.quantity)     # after this calculations we can add the offers based on these
            quantity = cart_item.quantity
            tax =(18* total)/100
            grand_total = total + tax
    except ObjectDoesNotExist:
        pass# we can simply pass it.
    
    context = {
        'total'         : total,
        'quantity'      : quantity,
        'cart_items'    : cart_items,
        'tax'           :tax,
        'grand_total'   : grand_total,
        
    }
    return render(request, 'cart_final.html', context)



