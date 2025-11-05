from django.db import models

from category.models import Category


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    images = models.ImageField(upload_to='images/products/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']
        verbose_name_plural = 'Products'
