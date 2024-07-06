from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("<str:slug>/view", ProductDetailView.as_view(), name="product_detail"),
    path("add/", ProductCreateView.as_view(), name="add_product"),
    path("<str:slug>/update/", ProductUpdateView.as_view(), name="update_product"),
    path("<str:slug>/delete/", ProductDeleteView.as_view(), name="delete_product"),
]
