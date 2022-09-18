from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cart,CartItem



class CartAdmin(admin.ModelAdmin):
    list_display =('cart_id','date_added')
    list_display_links =()
    readonly_fields =('cart_id','date_added')
    ordering = ('-date_added',)
    filter_horizontal = ()
    list_filter = ()    
    fieldsets = ()
    
    
class CartItemAdmin(admin.ModelAdmin):
    list_display =('cart','product', 'quantity', 'is_active')
    list_display_links =('product','cart')
    readonly_fields =('cart_id',)
    ordering = ()
    filter_horizontal = ()
    list_filter = ()    
    fieldsets = ()
    
    
    
    
# Register your models here.
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)