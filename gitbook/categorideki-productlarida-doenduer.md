# 🍳 Categorideki Productlarıda Döndür

## Burdan başlayabilirsin

`git checkout bc9579034ce523f3379714b0dbbdf771299ea8cb`

***

Linkte eğer <mark style="color:red;">**name**</mark> paremetresi var ise product detaylarını döndürmek için yeni bir serializer yazdım

{% code title="stock/serializers.py" %}
```python
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id', 'name', 'products', 'product_count')

    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()
```
{% endcode %}

Bu serializerı views.py bir paremetre olma koşuluna göre dödürücem bunun için _<mark style="color:orange;">get\_serializer\_class</mark>_ metodunu kullanıcam

```python
# ...
from .serializers import CategorySerializer, CategoryProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    # ...
    
    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return CategoryProductSerializer
        return super().get_serializer_class()
```

