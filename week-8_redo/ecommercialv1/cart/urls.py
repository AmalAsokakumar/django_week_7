from django.urls import path 
from .import views

urlpatterns = [
    path("", views.cart, name="view_cart"),
    path("add-cart/<int:product_id>/", views.add_cart, name="add_cart"),
    path("remove-cart/<int:product_id>/<int:cart_item_id>", views.remove_cart, name="remove_cart"),
    path("remove-cart-item/<int:product_id>/<int:cart_item_id>", views.remove_cart_item, name="remove_cart_item"),
]
