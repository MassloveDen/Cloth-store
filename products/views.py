from django.shortcuts import render
from products.models import Production,Catalog
# Create your views here.


def home(request):
    cont = {
        'title': 'Магазин'
    }
    return render(request, 'products/home.html', cont)


def merch(request):
    cont = {
        'title': 'Каталог товаров',
        'categor': Catalog.objects.all(),
        'merch': Production.objects.all(),
    }
    return render(request, 'products/merch.html', cont)




