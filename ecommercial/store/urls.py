from django.urls import path
from . import views 


urlpatterns = [
    path('',views.store, name='store'),
    path('<slug:category_slug>/',views.store, name='products_by_category'), # when ever the user request for a particular category, we are gonna make a url pattern( slug) that matches with the category to make that content available to the user.
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail, name='product_details'),# creating individual links for each product. c
]
