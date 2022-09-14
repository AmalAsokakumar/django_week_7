from django.db import models
import uuid

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)
    brand_slug = models.SlugField(unique=True, default=uuid.uuid1)
    description = models.TextField(max_length=255, blank=True)
    brand_image = models.ImageField(upload_to='photos/brand', blank=True)
    offer_status = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.brand_name
    