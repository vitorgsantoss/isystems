from django.contrib import admin
from tenants.models import Tenant, Address


class AdressInline(admin.TabularInline):
    model = Address
    extra = 1


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    inlines = [AdressInline]
