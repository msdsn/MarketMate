---
description: filter özelliği koymak
---

# 🪟 Fitreleme

### Enpoint:&#x20;

`http://127.0.0.1:8000/stock/categories/?name=Spor`

{% embed url="https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend" %}

## Bu noktadan başla

`git checkout 45a91cee108aabd7074f6219fd50d429fd175a4f`

***

```
pip install django-filter
```

```
INSTALLED_APPS = [
    ...
    'django_filters',
    ...
]
```

```python
# ...
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    # ...
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name']
```
