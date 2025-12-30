from django.db import models
from django.contrib.auth.models import User

class Tenant(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='tenant', on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name


class Adress(models.Model):
    tenant = models.ForeignKey(Tenant, verbose_name='adress', on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=7)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    def __str__(self):
        return f' Adress of {self.tenant}'