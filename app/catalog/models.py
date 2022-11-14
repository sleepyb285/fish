from django.db import models
from django.urls import reverse
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, help_text = "Название категории")
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to = 'uploads/category/', null = True, blank = True,)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'product_slug': self.slug})

class Provider(models.Model):
    name = models.CharField(max_length=255, help_text="Название поставщика")

    def __str__(self):
        return self.name

class Fish(models.Model):
    name = models.CharField(max_length=255, help_text="Название рыбы")
    price = models.IntegerField(help_text="Стоимость рыбы")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=0)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', null = True, blank = True,)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'product_slug': self.slug})
