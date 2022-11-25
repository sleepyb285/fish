from django.db import models
from django.urls import reverse
from phone_field import PhoneField
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, help_text = "Название категории")
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to = 'uploads/category/', null = True, blank = True,)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL, blank=True, null=True)
    CreateDate = models.DateField(auto_now_add=True)
    UpdateDate = models.DateField(auto_now=True, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'category_slug': self.slug})

class Provider(models.Model):
    name = models.CharField(max_length=255, help_text="Название поставщика")
    slug = models.SlugField(null=False, unique=True)
    CreateDate = models.DateField(auto_now_add=True)
    UpdateDate = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length=255, help_text="Название атрибута")
    CreateDate = models.DateField(auto_now_add=True)
    UpdateDate = models.DateField(auto_now=True, null=True)
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
    attributes = models.ManyToManyField(Attribute, through='FilterInfo', related_name='attributes')
    CreateDate = models.DateField(auto_now_add=True)
    UpdateDate = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fish-detail', kwargs={'fish_slug': self.slug})
    class Meta:
        ordering = ['-UpdateDate']
    

class FilterInfo(models.Model):
    rel_attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    rel_fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, help_text="Значение")
    show = models.BooleanField(default=0)
    def __str__(self):
        return self.value
    
    class Meta:
        ordering = ['rel_attribute']

class Feedback(models.Model):
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Введите ваше имя')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'uploads/comms/%Y/%m/%d/', null = True, blank = True)

class Location(models.Model):
    title = models.CharField(max_length=255, help_text='Название локации')
    adress = models.CharField(max_length=255, help_text='Адрес')
    number = models.CharField(max_length=255, help_text='Номер телефона')
    email = models.CharField(max_length=255, help_text='Адрес электронной почты')
    photo = models.ImageField(upload_to = 'uploads/locations/', null = True, blank = True)
    city = models.CharField(max_length=255, help_text='Населенный пункт', null = True)
    CreateDate = models.DateField(auto_now_add=True)
    UpdateDate = models.DateField(auto_now=True, null=True)

    class Meta:
        ordering = ['city']

class Callback_request(models.Model):
    name = models.CharField(max_length=255, help_text='Указанное имя')
    phone = PhoneField(help_text = 'Ваш номер телефона')
    email = models.CharField(max_length=255, help_text='Адрес электронной почты', null= True, blank= True)
    text = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True, blank=True)
    CreateDate = models.DateField(auto_now_add=True)
    #По идее, обновляться не должны, так что обновление не ставлю



class Feedback_generic(models.Model):
    name = models.CharField(max_length=100, help_text='Введите ваше имя')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'uploads/comms/%Y/%m/%d/', null = True, blank = True)