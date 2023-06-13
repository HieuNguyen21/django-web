from web.models import Category

def menu_links(request):
    link = Category.objects.all()
    return dict(request,link=link)