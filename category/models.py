from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=100, unique =True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    categoryImage = models.ImageField(upload_to='images/categories', blank=True, null=True)

    class Meta:
        ordering = ['categoryName']
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.categoryName


