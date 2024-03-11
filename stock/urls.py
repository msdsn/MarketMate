from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, BrandView, FirmView, ProductView, PurchasesView

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('brands', BrandView)
router.register('firms', FirmView)
router.register('products', ProductView)
router.register('purchases', PurchasesView)

urlpatterns = [
    path('', include(router.urls)),
]