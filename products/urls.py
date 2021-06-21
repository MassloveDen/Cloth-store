from django.urls import path

from products.views import merch

app_name = 'products'

urlpatterns = [

    path('', merch, name='merch'),


]