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

Kullanıcıyı serializer'a ekle ve ilgili product için stock güncelle

```python
class PurchasesView(viewsets.ModelViewSet):
    # ...
    def create(self, request, *args, **kwargs):
        # ...
        # increase stock
        purchase = request.data
        product = Product.objects.get(id=purchase['product_id'])
        product.stock += purchase['quantity']
        product.save()
        # --------------
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

## Deneme:

### &#x20;<mark style="background-color:red;">Dene:</mark>  `http://127.0.0.1:8000/stock/purchases/`

### &#x20;<mark style="background-color:red;">Veri:</mark> &#x20;

*   ```json
    {
    ```

    ```postman_json
        "firm_id": 1,
        "product_id": 1,
        "brand_id": 1,
        "quantity": 10,
        "price": 5
    }
    ```

