
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.product import views as product_views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'products',product_views.ProductView,'product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)