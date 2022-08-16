from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# is_defoult_header


def index(request):
    #  slideritsems categoryes products reviews

    siteset = {
        'kafe_description': SiteSettings.objects.get(key='kafe_description').context,
        'kafe_description_title': SiteSettings.objects.get(key='kafe_description_title').context,
        'kafe_description_long': SiteSettings.objects.get(key='kafe_description_long').context,
        'phone': SiteSettings.objects.get(key='phone').context,
        'email': SiteSettings.objects.get(key='email').context,
        'work_time': SiteSettings.objects.get(key='work_time').context,
        'work_days': SiteSettings.objects.get(key='work_days').context,
    }

    params = {
        'siteset': siteset,
        'is_defoult_header': False,
        'slideritsems': Sales.objects.filter(is_published=True),
        'categoryes': Category.objects.filter(is_published=True, is_on_front_page=True),
        'products': Product.objects.filter(is_published=True, is_on_front_page=True),
        'reviews': Review.objects.filter(is_published=True)
    }
    params['slideritsems_range'] = range(len(params['slideritsems']))
    return render(request, 'kafe/index.html', params)


def menu(request):
    #  slideritsems categoryes products reviews
    siteset = {
        'kafe_description': SiteSettings.objects.get(key='kafe_description').context,
        'kafe_description_title': SiteSettings.objects.get(key='kafe_description_title').context,
        'kafe_description_long': SiteSettings.objects.get(key='kafe_description_long').context,
        'phone': SiteSettings.objects.get(key='phone').context,
        'email': SiteSettings.objects.get(key='email').context,
        'work_time': SiteSettings.objects.get(key='work_time').context,
        'work_days': SiteSettings.objects.get(key='work_days').context,
    }

    params = {
        'siteset': siteset,
        'is_sub_page': True,
        'is_defoult_header': True,
        'slideritsems': Sales.objects.filter(is_published=True),
        'categoryes': Category.objects.filter(is_published=True),
        'products': Product.objects.filter(is_published=True),
    }
    params['slideritsems_range'] = range(len(params['slideritsems']))
    return render(request, 'kafe/menu.html', params)



def card(request):
    #  slideritsems categoryes products reviews
    siteset = {
        'kafe_description': SiteSettings.objects.get(key='kafe_description').context,
        'kafe_description_title': SiteSettings.objects.get(key='kafe_description_title').context,
        'kafe_description_long': SiteSettings.objects.get(key='kafe_description_long').context,
        'phone': SiteSettings.objects.get(key='phone').context,
        'email': SiteSettings.objects.get(key='email').context,
        'work_time': SiteSettings.objects.get(key='work_time').context,
        'work_days': SiteSettings.objects.get(key='work_days').context,
    }


    card_get = request.GET.get("card")
    card_list = card_get.split('#')
    card = []

    for el in card_list:
        prd_id, col = el.split(':')
        card.append({ 'prd': Product.objects.get(id=int(prd_id)), 'col': int(col) })


    params = {
        'siteset': siteset,
        'is_sub_page': True,
        'is_defoult_header': True,
        'slideritsems': Sales.objects.filter(is_published=True),
        'categoryes': Category.objects.filter(is_published=True),
        'products': Product.objects.filter(is_published=True),
        'card': card,
    }
    params['slideritsems_range'] = range(len(params['slideritsems']))

    return render(request, 'kafe/card.html', params)



def order(request):
    #  slideritsems categoryes products reviews
    siteset = {
        'kafe_description': SiteSettings.objects.get(key='kafe_description').context,
        'kafe_description_title': SiteSettings.objects.get(key='kafe_description_title').context,
        'kafe_description_long': SiteSettings.objects.get(key='kafe_description_long').context,
        'phone': SiteSettings.objects.get(key='phone').context,
        'email': SiteSettings.objects.get(key='email').context,
        'work_time': SiteSettings.objects.get(key='work_time').context,
        'work_days': SiteSettings.objects.get(key='work_days').context,
    }

    params = {
        'siteset': siteset,
        'is_sub_page': True,
        'is_defoult_header': True,
        'slideritsems': Sales.objects.filter(is_published=True),
        'categoryes': Category.objects.filter(is_published=True),
        'products': Product.objects.filter(is_published=True),
    }
    params['slideritsems_range'] = range(len(params['slideritsems']))
    return render(request, 'kafe/order.html', params)


def test(request):
    return  HttpResponse("Hello, World!") 


def about(request):
    #  slideritsems categoryes products reviews
    siteset = {
        'kafe_description': SiteSettings.objects.get(key='kafe_description').context,
        'kafe_description_title': SiteSettings.objects.get(key='kafe_description_title').context,
        'kafe_description_long': SiteSettings.objects.get(key='kafe_description_long').context,
        'phone': SiteSettings.objects.get(key='phone').context,
        'email': SiteSettings.objects.get(key='email').context,
        'work_time': SiteSettings.objects.get(key='work_time').context,
        'work_days': SiteSettings.objects.get(key='work_days').context,
    }

    params = {
        'siteset': siteset,
        'is_sub_page': True,
        'is_defoult_header': True,
        'slideritsems': Sales.objects.filter(is_published=True),
    }
    params['slideritsems_range'] = range(len(params['slideritsems']))
    return render(request, 'kafe/about.html', params)


