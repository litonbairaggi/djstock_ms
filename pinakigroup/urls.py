from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('store/', include('store.urls')),
    path('category/', include('category.urls')),
    path('supplier/', include('supplier.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)