
from django.urls import path
from tenants.views import home


app_name = 'tenants'

urlpatterns = [
    path('', home, name='home'),

] 

