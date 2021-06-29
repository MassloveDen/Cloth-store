from django.shortcuts import render, HttpResponseRedirect
from products.models import Production,Catalog, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    cont = {
        'title': 'Магазин'
    }
    return render(request, 'products/home.html', cont)


def merch(request, categor_id=None, page=1):
    contex = {'title': 'Каталог товаров',
        'categor': Catalog.objects.all(),
        }
    if categor_id:
        merch = Production.objects.filter(categor_id=categor_id)
    else:
        merch = Production.objects.all()
    paginator = Paginator(merch, 3)
    products_paginator = paginator.page(page)
    contex.update({'merch': products_paginator})
    return render(request, 'products/merch.html', contex)


@login_required
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


@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

