from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Product
from .forms import ProductForm


class ProductViewMixin:
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class ProductListView(LoginRequiredMixin, ProductViewMixin, ListView):
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 10


class ProductDetailView(LoginRequiredMixin, ProductViewMixin, DetailView):
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProductCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, ProductViewMixin, CreateView
):
    template_name = "products/product_form.html"
    permission_required = "products.add_product"
    success_url = reverse_lazy("products")


class ProductUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, ProductViewMixin, UpdateView
):
    template_name = "products/product_form.html"
    permission_required = "products.change_product"

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={"slug": self.object.slug})


class ProductDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, ProductViewMixin, DeleteView
):
    template_name = "products/product_confirm_delete.html"
    permission_required = "products.delete_product"
    success_url = reverse_lazy("product_list")
