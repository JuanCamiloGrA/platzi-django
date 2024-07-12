from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
)
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer


class ProductViewMixin:
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class ProductListView(ProductViewMixin, ListView):
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, ProductViewMixin, CreateView
):
    template_name = "products/product_form.html"
    permission_required = "products.add_product"
    success_url = reverse_lazy("products")


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
