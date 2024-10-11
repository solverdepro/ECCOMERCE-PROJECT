from .models import cartegory

def menu_links(request):
    links = cartegory.objects.all()
    return dict(links = links)
    