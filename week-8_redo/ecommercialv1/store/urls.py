from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from .import views



urlpatterns = [
    path('add',views.add_product, name = 'add_product'), # add_category/
    path('success/',views.upload_pic, name = 'product_success'),
    
    # admin store 
    path('product',views.view_product, name = 'product_view'),
    path('edit-product/<int:id>',views.edit_product, name = 'edit_product'),
    path('delete-product/<int:id>',views.delete_product, name ='delete_product'),
   
   
    # slug fields 
    path('',views.store, name='store'),
    path('<slug:category_slug>/',views.store, name='products_by_category'), # when ever the user request for a particular category, we are gonna make a url pattern( slug) that matches with the category to make that content available to the user.
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail, name='product_detail'),# creating individual links for each product. c
    
    # path('<slug:brand_slug>/',views.store, name='products_by_brand'),
    # path('<slug:brand_slug>/<slug:product_slug>/',views.product_detail, name='product_detail'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)