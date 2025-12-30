from django.contrib import admin
from tenants.models import Tenant, Adress


class AdressInline(admin.TabularInline):
    model = Adress
    extra = 1


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    inlines = [AdressInline]
