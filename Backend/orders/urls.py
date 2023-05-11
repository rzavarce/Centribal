from django.urls import path

from .views import OrdersViewset, OrdersDetailViewset, OrdersAddFormData, \
    OrdersEditFormData

urlpatterns = [
    path('orders/', OrdersViewset.as_view(), name='orders'),
    path('orders/<int:pk>/', OrdersDetailViewset.as_view(),
         name='orders_detail'),
    path('orders/add/', OrdersAddFormData.as_view(), name='order_add'),
    path('orders/edit/<int:pk>/', OrdersEditFormData.as_view(),
         name='order_edit'),
]

