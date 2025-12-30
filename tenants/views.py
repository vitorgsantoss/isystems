from django.shortcuts import render


def home(request, tenant_name):
    print(tenant_name)    
    return render(
        request, 
        'base_template.html'
    )