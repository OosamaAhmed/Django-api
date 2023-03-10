from django.db import models
from django.shortcuts import get_object_or_404

from category.models import Category


# class Category (models.Model):
#     name=



# Create your models here.

# stracture of table here in class
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='productapp/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 related_name='category_posts')
    def __str__(self):
        return self.name
    

    def get_image_url(self):
        return f"/media/{self.image}"
  
