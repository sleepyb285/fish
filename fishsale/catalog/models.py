from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50, help_text = "Введите категорию")
    def __str__(self):
        return self.name

class Goods(models.Model):
    name = models.CharField(max_length = 100, help_text = "Введите название товара")
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)

    
