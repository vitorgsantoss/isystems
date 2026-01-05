from django.contrib import admin
from sales.models import SaleItem, Sale


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    inlines = [SaleItemInline]
    exclude = 'value',
    list_display = 'tenant', 'payment_method', 'value'
