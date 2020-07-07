from django.db import models


# Create your models here.

class Television(models.Model):
    model_name = models.CharField(max_length=251, unique=True)
    brand_name = models.CharField(max_length=250)
    old_price = models.CharField(max_length=250)
    new_price = models.CharField(max_length=250)
    specification = models.TextField(max_length=500)
    desc = models.CharField(max_length=150, verbose_name='Description')
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ('-list_date',)


class Ac(models.Model):
    model_name = models.CharField(max_length=252, unique=True)
    brand_name = models.CharField(max_length=250)
    old_price = models.CharField(max_length=250)
    new_price = models.CharField(max_length=250)
    specification = models.TextField(max_length=500)
    desc = models.CharField(max_length=150, verbose_name='Description')
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ('-list_date',)


class Grinder(models.Model):
    model_name = models.CharField(max_length=253, unique=True)
    brand_name = models.CharField(max_length=250)
    old_price = models.CharField(max_length=250)
    new_price = models.CharField(max_length=250)
    specification = models.TextField(max_length=500)
    desc = models.CharField(max_length=150, verbose_name='Description')
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ('-list_date',)


class Camera(models.Model):
    model_name = models.CharField(max_length=254, unique=True)
    brand_name = models.CharField(max_length=250)
    old_price = models.CharField(max_length=250)
    new_price = models.CharField(max_length=250)
    specification = models.TextField(max_length=500)
    desc = models.CharField(max_length=150, verbose_name='Description')
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ('-list_date',)
