# 🛫 ilk endpoint

## Tam bu noktadan başla

`git clone git@github.com:msdsn/MarketMate.git`

`git checkout 0db0cd44d7aaf0b0d9f8b241141fff1e42f871a0`

[Kurulumu tamamla](yardimci-sayfalar/django-baslangic.md#localde-baslat)

***

{% code title="stock/serializers.py" %}
```python
from rest_framework import serializers
from .models import Category, Brand, Product, Firm, Purchases, Sales

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
```
{% endcode %}

{% code title="stock/views.py" %}
```python
from rest_framework import viewsets
from .models import Category, Brand, Product, Firm, Purchases, Sales
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
```
{% endcode %}

{% code title="stock/urls.py" %}
```python
from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
{% endcode %}

<mark style="background-color:green;">Artık endpointi deneyebiliriz.</mark>

<figure><img src=".gitbook/assets/Screen Shot 2024-03-06 at 23.08.57.png" alt=""><figcaption></figcaption></figure>

