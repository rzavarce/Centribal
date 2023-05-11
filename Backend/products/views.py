from .models import Products
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import ProductsSerializer, ProductsDetailSerializer, \
    ProductsHistorySerializer


class ProductsViewset(ListCreateAPIView):
    model = Products
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        last_product = Products.objects.last()
        pk = last_product.pk + 1 if last_product else 1
        name = self.request.data.get("name").capitalize().replace(" ", "_")
        reference = 'P-' + name + '-' + str(pk)
        serializer.is_valid(raise_exception=True)
        serializer.save(reference=reference)


class ProductsDetailViewset(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsDetailSerializer

    def perform_update(self, serializer):
        pk = self.kwargs['pk']
        name = self.request.data.get("name").capitalize().replace(" ", "_")
        reference = 'P-' + name + '-' + str(pk)
        serializer.save(reference=reference)


class ProductsAddFormData(APIView):

    def get(self, request,):
        """ GET Request to List Form Data"""

        form_data = dict()

        history_query = Products.history.all()[:5]
        form_data["products_history"] = \
            ProductsHistorySerializer(history_query, many=True).data

        return Response(form_data, status=status.HTTP_200_OK)


class ProductsEditFormData(APIView):

    def get(self, request, pk):
        """ GET Request to List Form Data"""

        form_data = dict()

        product = Products.objects.filter(id=pk)
        form_data["product_data"] = ProductsSerializer(product, many=True).data

        history_query = Products.history.all()[:5]
        form_data["products_history"] = \
            ProductsHistorySerializer(history_query, many=True).data

        return Response(form_data, status=status.HTTP_200_OK)

