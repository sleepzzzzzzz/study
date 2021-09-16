from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='описание')
    slug = models.SlugField(max_length=40)


class Addon(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена')
    slug = models.SlugField(max_length=40)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена')
    slug = models.SlugField(max_length=40)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL, null=True)
    addon = models.ManyToManyField("Addon")