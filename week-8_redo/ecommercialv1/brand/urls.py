from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
from .import views



urlpatterns = [
    path('add_brand/',views.add_product, name = 'brand_image_upload'),
    path('success/',views.upload_pic, name = 'brand_success'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)