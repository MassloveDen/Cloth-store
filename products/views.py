from django.shortcuts import render, HttpResponseRedirect
from products.models import Production,Catalog, Basket

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

def basket_add(request, product_id):
    product = Production.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    current_page = request.META.get('HTTP_REFERER')

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)

def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

