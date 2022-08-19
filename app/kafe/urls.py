from django.urls import path
 
from .views import *
 
urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
    path('card/', card, name='card'),
    path('order/', delivery_order, name='order'),
    path('order/', order, name='order'),
    path('test/', test, name='test'),
    path('items/<int:id>/', items, name='items'),
    path('ready/', ready_order, name='ready'),
]
