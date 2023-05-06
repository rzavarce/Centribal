from django.urls import path

from .views import ProductsViewset, ProductsDetailViewset

urlpatterns = [
    path('products/', ProductsViewset.as_view(), name='products'),
    path('products/<int:pk>/', ProductsDetailViewset.as_view(),
         name='products_detail'),
]

