from rest_framework import serializers
from .models import Category, Brand, Product, Firm, Purchases, Sales
import datetime

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()
    

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
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

        read_only_fields = ('stock',)

class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id', 'name', 'products', 'product_count')

    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()
    
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'image',
        )

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'address',
            'image',
        )

class PurchasesSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    firm = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    category = serializers.SerializerMethodField()
    time_hour = serializers.SerializerMethodField()
    time_day = serializers.SerializerMethodField()
    class Meta:
        model = Purchases
        fields = (
            'id',
            'user',
            'firm',
            'firm_id',
            'category',
            'product',
            'product_id',
            'brand',
            'brand_id',
            'quantity',
            'price',
            'price_total',
            'time_hour',
            'time_day',
            
        )

    def get_category(self, obj):
        # product = Product.objects.get(id=obj.product_id)
        # return Category.objects.get(id=product.category_id).name
        return obj.product.category.name
    
    def get_time_hour(self, obj):
        #return datetime.datetime.strftime(obj.created, '%H:%M')
        return obj.created.strftime('%H:%M')
    
    def get_time_day(self, obj):
        #return datetime.datetime.strftime(obj.created, '%Y-%m-%d')
        return obj.created.strftime("%Y-%m-%d")
    

class SalesSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    category = serializers.SerializerMethodField()
    time_hour = serializers.SerializerMethodField()
    time_day = serializers.SerializerMethodField()
    class Meta:
        model = Sales
        fields = (
            'id',
            'user',
            'category',
            'product',
            'product_id',
            'brand',
            'brand_id',
            'quantity',
            'price',
            'price_total',
            'time_hour',
            'time_day',
            
        )

    def get_category(self, obj):
        # product = Product.objects.get(id=obj.product_id)
        # return Category.objects.get(id=product.category_id).name
        return obj.product.category.name
    
    def get_time_hour(self, obj):
        #return datetime.datetime.strftime(obj.created, '%H:%M')
        return obj.created.strftime('%H:%M')
    
    def get_time_day(self, obj):
        #return datetime.datetime.strftime(obj.created, '%Y-%m-%d')
        return obj.created.strftime("%Y-%m-%d")
    
    

    