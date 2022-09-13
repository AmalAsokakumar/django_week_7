from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home, name='user_home'),
    # path('shop/',views.shop, name='user_shop'),
    path('contact/',views.contact, name='user_contact'),
    path('about/',views.about, name='user_about'),
    # path('forget-password/',views.forget_password, name='user_forget_password'),
    # path('login/',views.login, name='user_login'),
    # path('register/',views.register, name='user_register'),
]