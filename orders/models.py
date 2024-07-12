from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Order(models.Model):
    """Model definition for Order."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Order."""

        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.user} - {self.order_date}"


class OrderProduct(models.Model):
    """Model definition for OrderProduct."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        """Meta definition for OrderProduct."""

        verbose_name = "OrderProduct"
        verbose_name_plural = "OrderProducts"

    def __str__(self):
        return f"{self.order} - {self.product} - {self.quantity}"
