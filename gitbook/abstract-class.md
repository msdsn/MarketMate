# 🎁 Abstract Class

## Burdan Başla:

`git clone git@github.com:msdsn/MarketMate.git`

`git checkout af0b5db4a45bf61fbdf5dd26c0245dd756bbc935`

[Uygulamayı başlat](yardimci-sayfalar/django-baslangic.md#localde-baslat)

***

Bir çok model olduğunda bir abstract class yazıp bunu kullanabiliriz.

{% code title="stock/models.py" %}
```python
class UpdateCreate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Product(UpdateCreate):
    # ...
class Firm(UpdateCreate):
    # ...
class Purchases(UpdateCreate):
    # ...
class Sales(UpdateCreate):
    # ...
```
{% endcode %}

{% @github-files/github-code-block url="https://github.com/msdsn/MarketMate/raw/0db0cd44d7aaf0b0d9f8b241141fff1e42f871a0/stock/models.py" %}
