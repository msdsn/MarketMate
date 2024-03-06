---
description: Amacımız endpointe arama özelliği eklemek
---

# 🔎 Search özelliği

## Arama özellikli url:

`http://127.0.0.1:8000/stock/categories/?search=sp`

## Burdan başla

`git chechout 45a91cee108aabd7074f6219fd50d429fd175a4f`

***

Arama özelliği için viewsete iki tane şey eklemeliyiz.

{% code title="stock/views.py" %}
```python
from rest_framework import viewsets, filters
# ... [imports]

class CategoryViewSet(viewsets.ModelViewSet):
    # ... 
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
```
{% endcode %}
