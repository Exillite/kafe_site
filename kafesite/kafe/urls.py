from django.urls import path
 
from .views import *
 
urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
    path('card/', card, name='card'),
    path('order/', order, name='order'),
]
