from .models import Categoryv

def categories(request):
    return {
        'categories' : Category.objects.all()
            }
