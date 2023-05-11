from rest_framework.serializers import ModelSerializer
from .models import Products


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        read_only_fields = ('reference', 'created_date', 'modified_date',)
        fields = '__all__'


class ProductsDetailSerializer(ModelSerializer):
    class Meta:
        model = Products
        read_only_fields = ('reference', 'created_date', 'modified_date',)
        fields = '__all__'


class ProductsHistorySerializer(ModelSerializer):

    class Meta:
        model = Products.history.model
        fields = ('id', 'name', 'history_id', 'history_type',
                  'history_date', 'history_change_reason', 'history_user')
        depth = 1

