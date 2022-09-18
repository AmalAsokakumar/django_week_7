from django.db import models

# Create your models here.
from django.db import models
from category.models import Categories as category   # here w are using category as foreign key so we need to include it. 
from django.urls import reverse 
from brand.models import Brands as brand

# from brand.models import brand 
# Create your models here.

# for further reference
# 1  _ difference b/w  auto_add_now and auto_add. 




class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=255, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to = 'photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    offer_status    = models.BooleanField(default=False)
    category        = models.ForeignKey(category, on_delete=models.CASCADE) # (model_name, what to do when we delete this category) here the entire Field will be deleted when delete this particular field. 
    brand           = models.ForeignKey(brand, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add =True)
    modified_date   = models.DateTimeField(auto_now =True) 
    
    def get_url(self):
         return reverse('product_detail', args=[self.category.slug, self.slug])# here we have 2 arguments product slugs and categories slug. here self means this product and category is mentioned above and slug is from  category app ( we can access them because these fields are interconnected with : foreignkey . )   and second slug is this products slug.
    def __str__(self):
        return self.product_name
    
    
    
    
    
class VariationManager(models.Manager):
    def color(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    def size(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)
    
    
    
variation_category_choice = (                                                                                         # this is used to create a drop down variation list for the product.
    ('color','color'),
    ('size','size'),
)
    
    
    
class Variation(models.Model):
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category  = models.CharField(max_length=100, choices= variation_category_choice)
    variation_value     = models.CharField(max_length=100)
    is_active           = models.BooleanField(default=True)
    created_date        = models.DateTimeField(auto_now=True)
    
    objects = VariationManager()                                                                                        # only now will the two functions which are defined above will start working.
    
    # def __str__(self):
    #     self.variation_value
    def __unicode__(self):
      return self.variation_value