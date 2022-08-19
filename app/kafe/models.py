from email.policy import default
from pyexpat import model
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models

class Product(models.Model):
    # Описание модели одного товара
    name = models.CharField(max_length=255) # Название
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.FloatField() # Цена
    description = models.TextField(blank=True) # Описание
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/") # Фото
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    time_create = models.DateTimeField(auto_now_add=True) # Дата и время создания
    time_update = models.DateTimeField(auto_now=True) # Дата и время последнего редактирования
    is_published = models.BooleanField(default=True) # Доступно ли пользователям
    is_on_front_page = models.BooleanField(default=False) # Отоброжается ли на главной странице


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    is_published = models.BooleanField(default=False) # Доступно ли пользователям
    is_on_front_page = models.BooleanField(default=False) # Отоброжается ли на главной странице


class Sales(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    context = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True) # Фото
    is_published = models.BooleanField(default=False) # Доступно ли пользователям


class Review(models.Model):
    author_name = models.CharField(max_length=255)
    context = models.TextField()
    is_published = models.BooleanField(default=True) # Доступно ли пользователям


class SiteSettings(models.Model):
    key = models.CharField(max_length=255)
    context = models.TextField()
    time_update = models.DateTimeField(auto_now=True) # Дата и время последнего редактирования  


class Order(models.Model):
    isdelivery = models.BooleanField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    price = models.IntegerField(blank=True)
    address = models.TextField(blank=True)
    link = models.URLField(blank=True)
    card = models.TextField()
    isfinish = models.BooleanField(default=False)

