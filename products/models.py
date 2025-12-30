from django.db import models
from tenants.models import Tenant


class Category(models.Model):
    tenant = models.ForeignKey(Tenant, verbose_name='tenant', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    tenant = models.ForeignKey(Tenant, verbose_name='tenant', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50, null=True, blank=True)
    value = models.FloatField()
    stock = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.PROTECT)

    def __str__(self):
        return self.name
