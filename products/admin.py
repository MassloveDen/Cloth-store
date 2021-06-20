from django.contrib import admin

from products.models import Catalog, Production
# Register your models here.

admin.site.register(Catalog)
admin.site.register(Production)

