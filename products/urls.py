from django.urls import path

from products.views import merch, basket_add, basket_delete

app_name = 'products'

urlpatterns = [

    path('', merch, name='merch'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', basket_delete, name='basket_delete'),


]