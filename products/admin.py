from django.contrib import admin

from products.models import Catalog, Production, Basket

# Register your models here.

admin.site.register(Catalog)
admin.site.register(Basket)

@admin.register(Production)
class MerchAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quant', 'categor')
    fields = ('name', 'image', 'details', 'desc', ('price', 'quant'), 'categor')
    readonly_fields = ('desc',)
    ordering = ('name',)
    search_fields = ('name',)

class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'created_timestamp',)
    extra = 0



