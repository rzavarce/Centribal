from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from products.serializers import ProductsSerializer
from .models import Orders, OrderDetail
from products.models import Products
from .serializers import OrdersSerializer, OrdersDetailSerializer, \
    OrdersHistorySerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


def stock_validation(order_detail: dict):
    error_list = []
    for detail in order_detail:
        product = Products.objects.get(pk=detail['id'])
        if product.stock < detail['quantity']:
            error_list.append(
                "Product " + product.reference + " out of stock"
            )
    return error_list


def set_order_detail(order_detail: dict, order: Orders):
    for detail in order_detail:
        product = Products.objects.get(pk=detail['id'])
        order.price_total += product.price
        tax = product.price * product.tax / 100
        order.price_total_tax += product.price + tax
        OrderDetail(
            order=order,
            product=product,
            quantity=detail['quantity']
        ).save()
        product.stock -= detail['quantity']
        product.save()


class OrdersViewset(ListCreateAPIView):
    # model = Orders
    queryset = Orders.objects.all().order_by('id')
    serializer_class = OrdersSerializer

    def perform_create(self, serializer):

        order_detail = self.request.data['order_detail']
        error_list = stock_validation(order_detail)
        if error_list:
            raise ValidationError(error_list, code=status.HTTP_400_BAD_REQUEST)

        order = Orders(
            price_total=0,
            price_total_tax=0
        )
        order.save()

        set_order_detail(order_detail, order)
        order.save()
        return Response({
            'status': "OK",
            'message': 'Order have been created successfully',
            "order": OrdersSerializer(order).data
        },
            status=status.HTTP_201_CREATED,
        )


class OrdersDetailViewset(RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all().order_by('id')
    serializer_class = OrdersDetailSerializer

    def perform_create(self, serializer, pk=None):
        """
        """

        order_detail = self.request.data['order_detail']
        error_list = stock_validation(order_detail)
        if error_list:
            raise ValidationError(error_list, code=status.HTTP_400_BAD_REQUEST)

        order = Orders.objects.get(pk=pk)
        order.price_total = 0
        order.price_total_tax = 0
        order.order_detail.clear()

        set_order_detail(order_detail, order)
        order.save()
        return Response({
            'status': "OK",
            'message': 'Order have been updated successfully',
            "order": OrdersSerializer(order).data
        },
            status=status.HTTP_201_CREATED,
        )


class OrdersAddFormData(APIView):

    def get(self, request,):
        """ GET Request to List Form Data"""

        form_data = dict()

        products = Products.objects.filter(status=True)
        form_data["products_list"] = [
            {'value': product.id, 'label': product.name,
             'price': format(product.price, '.2f'),
             'tax': format(product.tax, '.2f')}
            for product in products
        ]

        history_query = Orders.history.all()[:5]
        form_data["orders_history"] = \
            OrdersHistorySerializer(history_query, many=True).data

        return Response(form_data, status=status.HTTP_200_OK)


class OrdersEditFormData(APIView):

    def get(self, request, pk):
        """ GET Request to List Form Data"""

        form_data = dict()

        order = Orders.objects.filter(id=pk)
        form_data["order_data"] = OrdersSerializer(order, many=True).data

        products = Products.objects.filter(status=True)
        form_data["products_list"] = [
            {'value': product.id, 'label': product.name,
             'price': format(product.price, '.2f'),
             'tax': format(product.tax, '.2f')}
            for product in products
        ]

        history_query = Orders.history.all()[:5]
        form_data["orders_history"] = \
            OrdersHistorySerializer(history_query, many=True).data

        return Response(form_data, status=status.HTTP_200_OK)

