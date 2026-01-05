from django.urls import path
from sales.views import CreateSalePDV


app_name = 'sales'

urlpatterns = [
    path('pdv/', CreateSalePDV.as_view(), name='pdv'),
]
