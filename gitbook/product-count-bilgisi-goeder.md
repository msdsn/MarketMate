---
description: Amacımız url e gittiğimizde categorilerdeki product sayılarını göstermek
---

# 🛒 Product Count Bilgisi Göder

### <mark style="color:purple;">end point:</mark> `http://127.0.0.1:8000/stock/categories/`

### <mark style="background-color:red;">Öncesi:</mark>

```json
[
    {
        "id": 1,
        "name": "Spor"
    }
]
```

Serializer'ı güncelliyorum

{% code title="stock/serializers.py" %}
```python
from rest_framework import serializers
from .models import Category, Brand, Product, Firm, Purchases, Sales

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()
```
{% endcode %}

### <mark style="background-color:red;">Sonrası:</mark>

```json
[
    {
        "id": 1,
        "product_count": 0,
        "name": "Spor"
    }
]
```
