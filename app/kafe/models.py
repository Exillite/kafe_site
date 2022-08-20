from email.policy import default
from pyexpat import model
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models

class Product(models.Model):
    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    # Описание модели одного товара
    name = models.CharField(max_length=255, verbose_name="Название товара") # Название
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.FloatField(verbose_name="Цена") # Цена
    description = models.TextField(blank=True, verbose_name="Описание") # Описание
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото") # Фото
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания") # Дата и время создания
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления") # Дата и время последнего редактирования
    is_published = models.BooleanField(default=True, verbose_name="Доступен") # Доступно ли пользователям
    is_on_front_page = models.BooleanField(default=False, verbose_name="Находится на главной странице") # Отоброжается ли на главной странице

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    is_published = models.BooleanField(default=False, verbose_name="Доступна") # Доступно ли пользователям
    is_on_front_page = models.BooleanField(default=False, verbose_name="Находится на главной странице") # Отоброжается ли на главной странице
    
    def __str__(self):
        return self.title


class Sales(models.Model):
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    context = models.TextField(verbose_name="Текст")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name="Фото") # Фото
    is_published = models.BooleanField(default=False, verbose_name="Доступно") # Доступно ли пользователям

    def __str__(self):
        return self.title

class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    author_name = models.CharField(max_length=255, verbose_name="Имя автора")
    context = models.TextField(verbose_name="Текст")
    is_published = models.BooleanField(default=True, verbose_name="Показывается") # Доступно ли пользователям



class SiteSettings(models.Model):
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

    key = models.CharField(max_length=255, verbose_name="Название")
    context = models.TextField(verbose_name="Текст")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновленя") # Дата и время последнего редактирования  

    def __str__(self):
        return self.key


class SitePhoto(models.Model):
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    key = models.CharField(max_length=255, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/site/%Y/%m/%d/", null=True, verbose_name="Фото")

    def __str__(self):
        return self.key


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['isfinish', 'time_create']

    isdelivery = models.BooleanField(verbose_name="Доставка курьером")
    name = models.CharField(max_length=255, verbose_name="Заказчик")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    price = models.IntegerField(blank=True, verbose_name="Итоговая сумма")
    address = models.TextField(blank=True, verbose_name="Адрес доставки")
    link = models.URLField(blank=True, verbose_name="Подробнее")
    card = models.TextField(verbose_name="Корзина")
    isfinish = models.BooleanField(default=False, verbose_name="завершён")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания") # Дата и время создания

