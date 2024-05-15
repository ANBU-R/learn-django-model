from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)
    sku = models.CharField(
        max_length=20, unique=True, verbose_name="Stock keeping unit"
    )

    def __str__(self) -> str:
        return self.name


# one to many
# one Product can have multiple images
class ProductImage(models.Model):
    product_image = models.ImageField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


# many to many
# one category can have multiple products
# one products can be in multiple category


class Category(models.Model):
    cat_name = models.CharField(max_length=20, verbose_name="Category name")
    products = models.ManyToManyField("Product")

    def __str__(self) -> str:
        return self.cat_name
