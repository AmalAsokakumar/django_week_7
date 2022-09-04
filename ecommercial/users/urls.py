from django.urls import path, include
from . import views 
urlpatterns = [
    path('',views.home, name='user_home'),
    path('shop/',views.shop, name='home_shop'),
    path('contact/',views.contact, name='user_contact'),
    path('about/',views.about, name='user_about'),
    # path('',views.home, name='home'),
    
]