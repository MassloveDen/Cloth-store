from django.shortcuts import render

# Create your views here.


def home(request):
    cont = {
        'title': 'Магазин'
    }
    return render(request, 'products/home.html', cont)


def merch(request):
    cont = {
        'title': 'Каталог товаров'
    }
    return render(request, 'products/merch.html', cont)


def test_cont(request):
    # return render(request, 'test.html')
    cont = {
        'title': 'store',
        'head': 'Welcome',
        'usver': 'Name surname',
        'list': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        'sails': True,
        'prod_on_sails': [
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.00},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590.00},
        ]
    }
    return render(request, 'products/test.html', cont)




