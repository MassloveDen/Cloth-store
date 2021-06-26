from django.contrib import admin

from products.models import Catalog, Production, Basket

# Register your models here.

admin.site.register(Catalog)
admin.site.register(Production)
admin.site.register(Basket)


