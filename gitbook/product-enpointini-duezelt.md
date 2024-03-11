# ⚾ Product enpointini düzelt

## Tam burdan başla

843ea533512ec44637a8d7c11859c658c4995781

***

<mark style="background-color:blue;">category</mark> ve <mark style="background-color:blue;">brand</mark> field ları id olarak değilde değer olarak döndürmek için bunu yapıyoruz

#### Öncesi

```json
[
    {
        "id": 1,
        "created": "2024-03-06T21:39:57.634717Z",
        "updated": "2024-03-06T21:39:57.634756Z",
        "name": "Bandana",
        "stock": 10,
        "category": 1,
        "brand": 1
    }
]
```

```python
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'category_id',
            'brand',
            'brand_id',
            'stock',
        )
```

#### Sonrası

```json
[
    {
        "id": 1,
        "name": "Bandana",
        "category": "Spor",
        "category_id": 1,
        "brand": "Adidas",
        "brand_id": 1,
        "stock": 10
    }
]
```
