from django.urls import path

from .views import ProductsViewset, ProductsDetailViewset, ProductsAddFormData, \
    ProductsEditFormData

urlpatterns = [
    path('products/', ProductsViewset.as_view(), name='products'),
    path('products/<int:pk>/', ProductsDetailViewset.as_view(),
         name='products_detail'),
    path('products/add/', ProductsAddFormData.as_view(), name='product_add'),
    path('products/edit/<int:pk>/', ProductsEditFormData.as_view(),
         name='product_edit'),
]

