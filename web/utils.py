# -*- coding: utf-8 -*-
from .models import News, Category, Asset, Purchase
import datetime

MONTHS = [
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря'
]

MONTHS_EN = [
    'january', 
    'february',
    'march',
    'april',
    'may', 
    'june', 
    'july', 
    'august',
    'september',
    'october',
    'november',
    'december'
]

MONTHS_KK = [
    'қаңтар',
    'ақпан',
    'yаурыз',
    'сәуір',
    'мамыр',
    'маусым',
    'шілде',
    'тамыз',
    'қыркүйек',
    'қазан',
    'қараша',
    'желтоқсан'
]

def increase_visits(asset):
    asset.visits += 1
    asset.save()
    return asset

def mapping_title(news):
    news.title = f'{news.title[:80]}...' if len(news.title) > 80 else news.title
    return news

def mapping_asset_price(asset):
    asset.price = asset.price.replace(' ', '')
    res = ''
    k = 0
    for i in range(len(str(asset.price)) - 1, -1, -1):
        res += str(asset.price)[i]
        k += 1
        if k % 3 == 0:
            res += ' '
    asset.price = res[::-1]

    return asset

def mapping_asset_perf_date(asset):
    b = asset.performance_date
    asset.performance_date = f"{ b.year }-{ b.month if b.month >= 10 else ('0' + str(b.month)) }-{ b.day if b.day >= 10 else ('0' + str(b.day)) } "
    return asset

def mapping_asset_creation_date(asset):
    b = asset.creation_date
    asset.creation_date = f"{ b.year }-{ b.month if b.month >= 10 else ('0' + str(b.month)) }-{ b.day if b.day >= 10 else ('0' + str(b.day)) } "
    asset.creation_date += f"{ b.hour if b.hour >= 10 else ('0' + str(b.hour))}:{ b.minute if b.minute >= 10 else ('0' + str(b.minute))}:{ b.second if b.second >= 10 else ('0' + str(b.second))}"
    return asset

def get_categories(categories):
    data = [ cat for cat in categories ]
    for cat in data:
        cat.count = Asset.objects.filter(
            category = cat.id, 
            state = True, 
            performance_date__gte = datetime.datetime.now()
        ).count()
    data = list(filter(
        lambda cat: cat.count > 0, 
        data
    ))
    return data

def mapping_purchase_creation_date(purchase):
    b = purchase.creation_date
    purchase.creation_date = f"{ b.year }-{ b.month if b.month >= 10 else ('0' + str(b.month)) }-{ b.day if b.day >= 10 else ('0' + str(b.day)) } "
    purchase.creation_date += f"{ b.hour if b.hour >= 10 else ('0' + str(b.hour))}:{ b.minute if b.minute >= 10 else ('0' + str(b.minute))}:{ b.second if b.second >= 10 else ('0' + str(b.second))}"
    return purchase

def mapping_purchase_description(purchase):
    if len(purchase.description) > 230:
        i = 230
        f = False
        ans = ''
        while i >= 0:
            if f:
                ans += purchase.description[i]
            elif purchase.description[i] == ' ':
                f = True
            i -= 1
        purchase.description = ans[::-1] + '...'
    return purchase

def mapping_news_creation_date(news):
    b = news.creation_date
    # news.creation_date = f"{ b.day } { b.strftime('%A') } { b.year }"
    return news

def mapping_news_creation_date_plural(news, lang):
    for n in news:
        b = n.creation_date
        if lang == 'kk':
            n.creation_date = f"{ b.day } { MONTHS_KK[b.month - 1] } { b.year }"
        elif lang == 'en':
            n.creation_date = f"{ b.day } { MONTHS_EN[b.month - 1] } { b.year }"
        else:
            n.creation_date = f"{ b.day } { MONTHS[b.month - 1] } { b.year }"
    return news

def get_asset_coordinates(asset):
    coordinates = str(asset.location)[
        str(asset.location).find('[') + 1:
        str(asset.location).find(']')
    ]
    return coordinates

def mapping_asset_location(asset):
    return str(asset.location)[:str(asset.location).find('[')]

def mapping_asset_location_2(asset):
    asset.location = str(asset.location)[:str(asset.location).find('[')]
    return asset