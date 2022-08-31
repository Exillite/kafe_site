from django.urls import path
 
from .views import *
 
urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
    path('card/', card, name='card'),
    path('orderdelibery/', delivery_order, name='orderdelibery'),
    path('order/', order, name='order'),
    path('test/', test, name='test'),
    path('items/<int:id>/', items, name='items'),
    path('finish/<int:id>/', finish, name='finish'),
    path('dd/<int:delay>/', dd),
    path('ready/', ready_order, name='ready'),
]
