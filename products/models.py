from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def has_variants(self):
        return self.variants.exists()


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants',
                                on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('product', 'size')

    def __str__(self):
        return f"{self.product.name} ({self.size})"
