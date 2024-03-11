# 🤩 Purchase yapıldığında stock güncelle

## Başlarken&#x20;

`git checkout 69cc580723dca14a67ef0d907b718e5a6e43b1f3`

***

Model viewdaki create metodunu override adelim

```python
#...
from rest_framework.response import Response
from rest_framework import status

# ...

class PurchasesView(viewsets.ModelViewSet):
    # ...

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # increase stock
        # --------------
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
```

## Increase Stock:

