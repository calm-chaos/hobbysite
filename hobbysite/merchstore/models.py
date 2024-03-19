from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    name = models.CharField(max_length=225)
    desc = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=225)

    product_type = models.ForeignKey(
        "ProductType", null=True, on_delete=models.SET_NULL, related_name="product"
    )

    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("merchstore:product", args=[self.pk])

    class Meta:
        ordering = ["name"]
