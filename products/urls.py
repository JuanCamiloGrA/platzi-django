from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductListAPI,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("api/", ProductListAPI.as_view(), name="products_api"),
    path("add/", ProductCreateView.as_view(), name="add_product"),
]
