from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
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
    if card_get != "":
        card_list = card_get.split('s')
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
            'card_len': card_get,
            'is_empty_card': False,
        }
    else:
        params = {
            'siteset': siteset,
            'is_sub_page': True,
            'is_defoult_header': True,
            'slideritsems': Sales.objects.filter(is_published=True),
            'categoryes': Category.objects.filter(is_published=True),
            'products': Product.objects.filter(is_published=True),
            'is_empty_card': True,
        }


    params['slideritsems_range'] = range(len(params['slideritsems']))

    return render(request, 'kafe/card.html', params)



def delivery_order(request):
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
    card_list = card_get.split('s')
    card = []

    total_prs = 0
    for el in card_list:
        prd_id, col = el.split(':')
        prd = Product.objects.get(id=int(prd_id))
        total_prs += prd.price
        card.append({ 'prd': prd, 'col': int(col) })

    total_prs = int(total_prs)

    params = {
        'siteset': siteset,
        'is_sub_page': True,
        'is_defoult_header': True,
        'slideritsems': Sales.objects.filter(is_published=True),
        'categoryes': Category.objects.filter(is_published=True),
        'products': Product.objects.filter(is_published=True),
        'card': card,
        'card_len': card_get,
        'total_prs': total_prs,
        'total_col': len(card),
        'card_str': card_get,
    }
    params['slideritsems_range'] = range(len(params['slideritsems']))
    return render(request, 'kafe/delivery_order.html', params)

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

    card_get = request.GET.get("card")
    card_list = card_get.split('s')
    card = []

    total_prs = 0
    for el in card_list:
        prd_id, col = el.split(':')
        prd = Product.objects.get(id=int(prd_id))
        total_prs += prd.price
        card.append({ 'prd': prd, 'col': int(col) })

    total_prs = int(total_prs)

    params = {
        'siteset': siteset,
        'is_sub_page': True,
        'is_defoult_header': True,
        'slideritsems': Sales.objects.filter(is_published=True),
        'categoryes': Category.objects.filter(is_published=True),
        'products': Product.objects.filter(is_published=True),
        'card': card,
        'card_len': card_get,
        'total_prs': total_prs,
        'total_col': len(card),
        'card_str': card_get,
    }
    params['slideritsems_range'] = range(len(params['slideritsems']))
    return render(request, 'kafe/order.html', params)

def test(request):
    s1 = SiteSettings(key='kafe_description', context='''Обычно люди приходят в Додо Пиццу, чтобы просто поесть. Наши промоутеры раздают листовки про кусочек пиццы за двадцать рублей или ещё что-то выгодное. Мы делаем это как первый шаг, чтобы познакомиться.

Но для нас Додо — не только пицца. Это и пицца тоже, но в первую очередь это большое дело, которое вдохновляет нас, заставляет каждое утро просыпаться и с интересом продолжать работу.

В чём же наш интерес? Сейчас расскажем.''')
    s1.save()
    s2 = SiteSettings(key='kafe_description_title', context='Мы - лучшие!')
    s2.save()
    s3 = SiteSettings(key='kafe_description_long', context='''Вкусные роллы, горячая лапша и закуски в Брянске!
Мы покорим Вас вкусом, так как готовим из самых свежих продуктов, а главным ингредиентом наших блюд является любовь к своему делу!

Обычно люди приходят в Додо Пиццу, чтобы просто поесть. Наши промоутеры раздают листовки про кусочек пиццы за двадцать рублей или ещё что-то выгодное. Мы делаем это как первый шаг, чтобы познакомиться. Но для нас Додо — не только пицца. Это и пицца тоже, но в первую очередь это большое дело, которое вдохновляет нас, заставляет каждое утро просыпаться и с интересом продолжать работу. В чём же наш интерес? Сейчас расскажем.''')
    s3.save()
    s4 = SiteSettings(key='phone', context='+7 (900) 372-99-66')
    s4.save()
    s5 = SiteSettings(key='email', context='example@gmail.com')
    s5.save()
    s6 = SiteSettings(key='work_time', context='10:30 - 22:30')
    s6.save()
    s7 = SiteSettings(key='work_days', context='Вторник - Воскресение')
    s7.save()
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


def ready_order(request):
    if request.method == 'POST':
        name = request.POST["firstname"]
        phone = request.POST["phone"]
        is_delivery = request.POST["is_delivery"]
        card = request.POST["card"]
        if is_delivery == "yes":
            address = request.POST["address"]
            state = request.POST["state"]
            zipp = request.POST["zip"]

        new_order = Order()

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
        }

        return render(request, 'kafe/ready_order.html', params)
    else:
        return HttpResponseNotFound("Страница не найдена.")



# def items(request):
#     siteset = {
#         'kafe_description': SiteSettings.objects.get(key='kafe_description').context,
#         'kafe_description_title': SiteSettings.objects.get(key='kafe_description_title').context,
#         'kafe_description_long': SiteSettings.objects.get(key='kafe_description_long').context,
#         'phone': SiteSettings.objects.get(key='phone').context,
#         'email': SiteSettings.objects.get(key='email').context,
#         'work_time': SiteSettings.objects.get(key='work_time').context,
#         'work_days': SiteSettings.objects.get(key='work_days').context,
#     }

#     params = {
#         'siteset': siteset,
#         'is_sub_page': True,
#         'is_defoult_header': True,
#     }




