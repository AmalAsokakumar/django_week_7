from django.urls import path
from . import views 

urlpatterns = [
    
                        # needed some modifications
    # user login and logouts 
    # path('forget-password/',views.forget_password, name='user_forget_password'),
    # path('login/',views.login, name='user_login'),
    # path('register/',views.register, name='user_register'),
        

                         # admin
    path('list-users/',views.list_users, name='user_list'),
    path('register/',views.register, name= 'register'),
    path('login',views.admin_login, name= 'admin_login'),
    path('admin-logout/',views.admin_logout, name= 'admin_logout'),
    path('',views.admin_home, name= 'admin_home')
]