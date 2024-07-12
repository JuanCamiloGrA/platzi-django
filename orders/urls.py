from django.urls import path

from .views import OrderDetailView, OrderProductCreateView

urlpatterns = [
    path("my-order/", OrderDetailView.as_view(), name="my_order"),
    path("add-product/", OrderProductCreateView.as_view(), name="add_product"),
]
