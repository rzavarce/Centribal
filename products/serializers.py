from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields = ('created_date', 'modified_date',)


class ProductsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        read_only_fields = ('reference', 'created_date', 'modified_date',)
        fields = '__all__'
