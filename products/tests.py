from django.test import TestCase, Client
from django.urls import reverse
from .models import Product


class ProductListViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("products")
        self.product1 = Product.objects.create(name="Coffee", price=10.0)
        self.product2 = Product.objects.create(name="Tea", price=5.0)

    def test_product_list_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_product_list_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "products/product_list.html")

    def test_product_list_view_context(self):
        response = self.client.get(self.url)
        self.assertIn("products", response.context)
        self.assertEqual(len(response.context["products"]), 2)
        self.assertEqual(response.context["products"][0], self.product1)
        self.assertEqual(response.context["products"][1], self.product2)
