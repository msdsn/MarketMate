# ❤️‍🔥 Purchases için endpoint yap

## Tam burdan başla

184b6b421ef2cd70e53b752e8e2040ab6107146b

***

Signals ile <mark style="background-color:green;">price\_total</mark> değişkenini hesaplıcaz.

{% code title="stock/signals.py" %}
```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Purchases

@receiver(pre_save, sender=Purchases)
def calculate_total_price(sender, instance, **kwargs):
    instance.price_total = instance.quantity * instance.price
```
{% endcode %}

Signali geçerli kılmak için apps.py dosyasına bir şey ekliyoruz

{% code title="stock/apps.py" %}
```python
# ...
class StockConfig(AppConfig):
    # ...
    def ready(self):
        import stock.signals
```
{% endcode %}

### Serializerım:

```python
class PurchasesSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    firm = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    class Meta:
        model = Purchases
        fields = (
            'id',
            'user',
            'user_id',
            'firm',
            'firm_id',
            'product',
            'product_id',
            'brand',
            'brand_id',
            'quantity',
            'price',
            'price_total',
            'created',
            'updated'
        )
```

### View:

```python
class PurchasesView(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['product', 'firm']
    filterset_fields = ['product', 'firm']
```

### Endpoint:

```python
# ...
from .views import CategoryViewSet, BrandView, FirmView, ProductView, PurchasesView

# ...
router.register('purchases', PurchasesView)
# ...
```
