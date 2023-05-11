from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Orders, OrderDetail


class DetailSerializer(ModelSerializer):
    id = ReadOnlyField(source='product.id')
    reference = ReadOnlyField(source='product.reference')
    name = ReadOnlyField(source='product.name')

    class Meta:
        model = OrderDetail
        fields = ('id', 'reference', 'name', 'quantity')


class OrdersSerializer(ModelSerializer):
    order_detail = DetailSerializer(source='orderdetail_set', many=True,)

    class Meta:

        model = Orders
        read_only_fields = ('reference', 'price_total', 'price_total_tax',
                            'created_date', 'modified_date',)
        fields = ['id', 'reference', 'order_detail', 'price_total',
                  'price_total_tax', 'created_date',]


class OrdersDetailSerializer(ModelSerializer):
    order_detail = DetailSerializer(source='orderdetail_set', many=True, )

    class Meta:
        model = Orders
        read_only_fields = ('reference', 'price_total', 'price_total_tax',
                            'created_date', 'modified_date',)
        fields = ['reference', 'order_detail', 'price_total',
                  'price_total_tax', ]


class OrdersHistorySerializer(ModelSerializer):

    class Meta:
        model = Orders.history.model
        fields = ('id', 'reference', 'history_id', 'history_type',
                  'history_date', 'history_change_reason', 'history_user')
        depth = 1

