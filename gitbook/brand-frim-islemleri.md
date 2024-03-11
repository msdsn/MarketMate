# 📙 Brand - Frim islemleri

## Tam burdan başla

`git checkout 6fc35733ae9703413f5901771ad4c798ed9be044`

***

```python
#..
from .views import CategoryViewSet, BrandView, FirmView, ProductView
#...
router.register('brands', BrandView)
router.register('firms', FirmView)
router.register('products', ProductView)
```

```python
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'image',
        )

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'address',
            'image',
        )

    
```

```python
# ...
from .serializers import CategorySerializer, CategoryProductSerializer, BrandSerializer, FirmSerializer, ProductSerializer
# ...
class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['category', 'brand']
```
