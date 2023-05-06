from .models import Products
from .serializers import ProductsSerializer, ProductsDetailSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class ProductsViewset(ListCreateAPIView):
    model = Products
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        pk = Products.objects.last().pk + 1
        name = self.request.data.get("name").capitalize().replace(" ", "_")
        reference = 'P-' + name + '-' + str(pk)
        serializer.save(reference=reference)


class ProductsDetailViewset(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializer

    def perform_update(self, serializer):
        pk = self.kwargs['pk']
        name = self.request.data.get("name").capitalize().replace(" ", "_")
        reference = 'P-' + name + '-' + str(pk)
        serializer.save(reference=reference)
