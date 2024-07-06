from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("add/", ProductCreateView.as_view(), name="add_product"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="update_product"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product"),
]
