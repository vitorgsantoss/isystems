from django.db import models
from tenants.models import Tenant
from products.models import Product


class Desk(models.Model):
    tenant = models.ForeignKey(Tenant, related_name="tenant", on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    number = models.IntegerField()
    products = models.ManyToManyField(Product)
    active = models.BooleanField(default=False)
    


class Sale(models.Model):
    PAYMENT_CHOICES = [
        (1, 'Crédito'),
        (2, 'Débito'),
        (3, 'Pix'),
        (4, 'Dinheiro')
    ]
    payment_method = models.IntegerField(choices=PAYMENT_CHOICES)
    client_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

