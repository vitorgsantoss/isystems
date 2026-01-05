from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:tenant_name>/', include('tenants.urls')),
    path('<str:tenant_name>/products/', include('products.urls')),
    path('<str:tenant_name>/sales/', include('sales.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
