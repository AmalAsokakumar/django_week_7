from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from .import views



urlpatterns = [
    path('',views.add_category, name = 'add_category'), # add_category/
    path('success/',views.upload_pic, name = 'category_success'),
    path('view/',views.view_category, name = 'category_view'),
    
    path('edit-category/<int:id>',views.edit_category, name = 'edit_category'),
    path('delete-category/<int:id>',views.delete_category, name ='delete_category'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)