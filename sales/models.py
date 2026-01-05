from django.db import models
from tenants.models import Tenant
from products.models import Product


class Sale(models.Model):
    tenant = models.ForeignKey(Tenant, related_name="sales", on_delete=models.CASCADE)
    desk_number = models.PositiveIntegerField()
    client_name = models.CharField(max_length=100, null=True, blank=True)
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.IntegerField(
        choices=[
            (1, 'Crédito'),
            (2, 'Débito'),
            (3, 'Pix'),
            (4, 'Dinheiro')
        ],
        null=True,
        blank=True
    )

    @property
    def value(self):
        items = self.items.select_related('product')
        return sum(item.product.value * item.quantity for item in items)

    def __str__(self):
        return f'{self.tenant}: R$ {self.value:.2f} - {self.created_at.date()}'


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
