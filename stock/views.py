from rest_framework import viewsets, filters
from .models import Category, Brand, Product, Firm, Purchases, Sales
from .serializers import CategorySerializer, CategoryProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['name']

    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return CategoryProductSerializer
        return super().get_serializer_class()
