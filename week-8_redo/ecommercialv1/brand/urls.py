from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from .import views



urlpatterns = [
    path('add/',views.add_brand, name = 'add_brand'),
    path('success/',views.upload_pic, name = 'brand_success'),
    path('',views.view_brand, name = 'brand_view'),
    path('edit-brand/<int:id>',views.edit_brand, name = 'edit_brand'),
    path('delete-brand/<int:id>',views.delete_brand, name ='delete_brand'),
    path('delete',views.delete_brand, name ='delete_brand'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)