from .models import brand

def menu_link(request):
    
    link = brand.objects.all()
    return dict(links=links)