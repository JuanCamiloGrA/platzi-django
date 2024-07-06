from django.db import models
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(max_length=255, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    image = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="Imagen")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Slug")

    class Meta:
        """Meta definition for Product."""

        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        """Override save method to generate slug."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
