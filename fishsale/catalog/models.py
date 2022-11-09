from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 250, help_text = "Введите категорию")
    slug = models.SlugField (null=False, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
          return reverse('category-detail', args=[str(self.id)])

class Location(models.Model):
    name = models.CharField(max_length = 250, help_text = 'Введите место вылова рыбы')
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 250, help_text = "Введите название товара")
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    location = models.ForeignKey(Location,on_delete = models.SET_NULL, null = True)
    price = models.IntegerField(null=True, help_text = "Введите стоимость рыбы")
    active = models.BooleanField(default = 0)
    image = models.ImageField(null = True, upload_to = 'images/', blank = True)
    slug = models.SlugField (null=False, unique=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'product_slug': self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
        #Кстати, вот это вот не может быть причиной нерабочих слагов? в админке они автофиллы, а после сохранения снова кириллица?
    def placeholder(self):
        pass
        
    class Meta:
        ordering = ["-price"]