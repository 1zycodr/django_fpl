# -*- coding: utf-8 -*-
# coding: utf8
from django.shortcuts import render
from django.db.models import Q
import requests, datetime, os
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import News, Asset, Category, Purchase, Results, Region, FinOtchet, Audit, Document, Page, Government, Directors

from django.template import RequestContext
from .utils import (
    mapping_title, mapping_asset_price, 
    mapping_asset_perf_date, mapping_asset_creation_date,
    get_categories, mapping_purchase_creation_date,
    mapping_purchase_description,
    mapping_news_creation_date,
    get_asset_coordinates,
    mapping_asset_location, 
    mapping_asset_location_2,
    increase_visits
)

def index(request):
    r = list(Region.objects.extra(select={'length':'Length(name)'}).order_by('length'))
    r.insert(0, r[2])
    del r[3]

    data = {
        'news_list' : map(
            mapping_news_creation_date,
            map(
                mapping_title, 
                News.objects.all().order_by('-creation_date')[:6]
            )
        ), 
        'sel_categories' : Category.objects.all(),
        'sel_regions' : r
    }
    
    if request.method in ['POST', 'GET']:
        try:
            name = request.GET['fullname']
        except Exception as ex:
            name = 'Неизвестный'

        try:
            phone = request.GET['phone']
        except Exception as ex:
            phone = 'Неизвестен'

        try:
            email = request.GET['email']
        except Exception as ex:
            email = 'Неизвестен'
        
        try:
            user_message = request.GET['message']
        except Exception as ex:
            user_message = 'Пусто'
        
        if phone != 'Неизвестен':
            message = f"""
            Имя: { name }
            Почта: { email }
            Номер телефона: { phone }
            Сообщение: \n { user_message }
            """

            try:
                send_mail('Заявка с сайта', message, 'sergeifadr@gmail.com', ['5zamiggos@gmail.com', 'info@fpl.kz'])
            except Exception as ex:
                print(ex)

    data['title'] = 'ФОНД ПРОБЛЕМНЫХ КРЕДИТОВ'
    return render(request, 'web/index.html', data)

def sitemap_page(request):
    return HttpResponse(open('/var/www/fpl.kz/web/templates/web/sitemap.xml').read(), content_type='application/xml')

def inf_page(request):
    return render(request, 'web/infographics.html')
    
def search_page(request):
    data = {
        'assets': [],
        'news': [],
        'zakupki': [],
        'itogi': [], 
        'documents': [],
        'pages' : []
    }

    if request.method == 'GET':
        try:
            find = request.GET['find']
        except Exception:
            find = None
        
        if find is not None:
            data['assets'] = map(
                mapping_asset_perf_date,
                list(
                    map(
                        mapping_asset_price, 
                        list(map( increase_visits, Asset.objects.filter(
                            Q(title__icontains=find) | 
                            Q(description__icontains=find) | 
                            Q(category__in = Category.objects.filter(
                                Q(name__icontains=find)
                            )) | 
                            Q(region__in = Region.objects.filter(
                                Q(name__icontains=find)
                            )),
                            state = True, 
                            performance_date__gte = datetime.datetime.now()
                        )))
                    )
                )
            )

            data['pages'] = Page.objects.filter(
                Q(title__icontains = find) | 
                Q(tags__icontains = find)
            )
            
            data['news'] = map(
                mapping_news_creation_date,
                map(
                    mapping_title, 
                    News.objects.filter(
                        Q(title__icontains = find) | 
                        Q(description__icontains = find)
                    ).order_by('-creation_date')
                )
            )

            data['zakupki'] = map(
                mapping_purchase_description,
                map(
                    mapping_purchase_creation_date,
                    Purchase.objects.filter(
                        Q(title__icontains = find) |
                        Q(description__icontains = find)
                    )
                )
            )

            data['itogi'] = map(
                mapping_purchase_description,
                map(
                    mapping_purchase_creation_date,
                    Results.objects.filter(
                        Q(title__icontains = find) |
                        Q(description__icontains = find)
                    )
                )
            ) 

            data['documents'] = Document.objects.filter(
                Q(title__icontains = find) |
                Q(tags__icontains = find)
            )
    
    for k, v in data.items():
        data[k] = list(v)
    
    return render(request, 'web/search-page.html', data)

def actives_page(request):
    r = list(Region.objects.extra(select={'length':'Length(name)'}).order_by('length'))
    r.insert(0, r[2])
    del r[3]

    data = {
        'categories' : get_categories(
            Category.objects.all()
        ),
        'sel_categories' : Category.objects.all(),
        'sel_regions' : r
    }

    if request.method == 'GET':
        try:
            find = request.GET['find']
        except Exception:
            find = None
	
        try:
            type = request.GET['type']
        except Exception:
            type = 'default'
        
        try:
            category = request.GET['category']
        except Exception:
            category = 'default'
        
        try:
            region = request.GET['region']
        except Exception:
            region = 'default'

        if find is None or find == '':
            if type == 'default' and category == 'default' and region == 'default':
                data['assets_list'] = map(
                    mapping_asset_perf_date,
                    list(
                        map(
                            mapping_asset_price, 
                            list(map(increase_visits, Asset.objects.filter(state=True, performance_date__gte = datetime.datetime.now()).order_by('-creation_date')))
                        )
                    )
                )
            elif type != 'default' and category != 'default' and region != 'default':
                data['assets_list'] = map(
                    mapping_asset_perf_date,
                    list(
                        map(
                            mapping_asset_price, 
                            list(map(increase_visits, Asset.objects.filter(
                                as_type = type, 
                                category = Category.objects.filter(pk=int(category))[0], 
                                region = Region.objects.filter(pk=int(region))[0], 
                                state = True, 
                                performance_date__gte = datetime.datetime.now()
                            )))
                        )
                    )
                )
            elif type != 'default' and category != 'default':
                data['assets_list'] = map(
                    mapping_asset_perf_date,
                    list(
                        map(
                            mapping_asset_price, 
                            list(map(increase_visits, Asset.objects.filter(
                                as_type = type, 
                                category = Category.objects.filter(pk=int(category))[0],
                                state = True, 
                                performance_date__gte = datetime.datetime.now()
                            )))
                        )
                    )
                )
            elif type != 'default' and region != 'default':
                data['assets_list'] = map(
                    mapping_asset_perf_date,
                    list(
                        map(
                            mapping_asset_price, 
                            list(map(increase_visits, Asset.objects.filter(
                                as_type = type, 
                                region = Region.objects.filter(pk=int(region))[0], 
                                state = True, 
                                performance_date__gte = datetime.datetime.now()
                            )))
                        )
                    )
                )
            elif category != 'default' and region != 'default':
                data['assets_list'] = map(
                    mapping_asset_perf_date,
                    list(
                        map(
                            mapping_asset_price, 
                            list(map(increase_visits, Asset.objects.filter(
                                category = Category.objects.filter(pk=int(category))[0], 
                                region = Region.objects.filter(pk=int(region))[0], 
                                state = True, 
                                performance_date__gte = datetime.datetime.now()
                            )))
                        )
                    )
                )
            elif category != 'default':
                data['assets_list'] = map(
                    mapping_asset_perf_date,
                    list(
                        map(
                            mapping_asset_price, 
                            list(map(increase_visits, Asset.objects.filter(
                                category = Category.objects.filter(pk=int(category))[0], 
                                state = True, 
                                performance_date__gte = datetime.datetime.now()
                            )))
                        )
                    )
                )
            elif type != 'default':
                data['assets_list'] = map(
                    mapping_asset_perf_date,
                    list(
                        map(
                            mapping_asset_price, 
                            list(map(increase_visits, Asset.objects.filter(
                                as_type = type, 
                                state = True, 
                                performance_date__gte = datetime.datetime.now()
                            )))
                        )
                    )
                )
            elif region != 'default':
                data['assets_list'] = map(
                    mapping_asset_perf_date,
                    list(
                        map(
                            mapping_asset_price, 
                            list(map(increase_visits, Asset.objects.filter(
                                region = Region.objects.filter(pk=int(region))[0],
                                state = True, 
                                performance_date__gte = datetime.datetime.now()
                            )))
                        )
                    )
                )
            else: 
                data['assets_list'] = []
        else:
            data['assets_list'] = map(
                mapping_asset_perf_date,
                list(
                    map(
                        mapping_asset_price, 
                        list(map( increase_visits, Asset.objects.filter(
                            Q(title__icontains=find) | 
                            Q(description__icontains=find) | 
                            Q(category__in = Category.objects.filter(
                                Q(name__icontains=find)
                            )) | 
                            Q(region__in = Region.objects.filter(
                                Q(name__icontains=find)
                            )),
                            state = True, 
                            performance_date__gte = datetime.datetime.now()
                        )))
                    )
                )
            )

    data['assets_list'] = list(map(
        mapping_asset_location_2,
        data['assets_list']
    ))
    
    return render(request, 'web/actives_page.html', data)

def news_item_page(request, pk):
    data = {
        'news' : mapping_news_creation_date(News.objects.get(pk=pk))
    }
    return render(request, 'web/news-item.html', data)

def active_page(request, pk):
    r = list(Region.objects.extra(select={'length':'Length(name)'}).order_by('length'))
    r.insert(0, r[2])
    del r[3]

    asset = mapping_asset_price(
        mapping_asset_perf_date(
            mapping_asset_creation_date(
                Asset.objects.get(pk=pk)
            )
        )
    )

    data = {
        'active' : asset,
        'sel_categories' : Category.objects.all(),
        'sel_regions' : r,
        'coordinates' : get_asset_coordinates(asset),
        'location' : mapping_asset_location(asset)
    }

    return render(request, 'web/active_page.html', data)

def ofond_page(request):
    return render(request, 'web/ofond.html')

def main_info_page(request):
    return render(request, 'web/main-info.html')

def org_struktura_page(request):
    return render(request, 'web/org-struktura.html')

def strateg_napr_page(request):
    return render(request, 'web/strateg-napr.html')

def rukovodstvo2_page(request):
    data = {
        'directors' : Directors.objects.all() 
    }
    return render(request, 'web/rukovodstvo2.html', data)

def dir_page(request, pk):
    data = {
        'gm' : Directors.objects.get(pk=pk)
    }

    return render(request, 'web/dirpage.html', data)

def sostav_pravlenia_page(request):
    data = {
        'government_members' : Government.objects.all()
    }

    return render(request, 'web/sostav-pravlenia.html', data)

def comitet_func_page(request):
    return render(request, 'web/comitet-func.html')

def riski_page(request):
    return render(request, 'web/riski.html')
 
def kodeks_page(request):
    return render(request, 'web/kodeks.html')
 
def principi_page(request):
    return render(request, 'web/principi.html')
 
def build_page_divi_page(request):
    return render(request, 'web/build-page-divi.html')
 
def build_page_razv_page(request):
    return render(request, 'web/build-page-razv.html')
 
def akti_page(request):
    return render(request, 'web/akti.html')
 
def audit_page(request):
    data = {
        'i_list' : Audit.objects.order_by('-title')
    }
    return render(request, 'web/audit.html', data)
 
def godovoi_otchet_page(request):
    data = {
        'o_list' : FinOtchet.objects.all()
    }
    return render(request, 'web/godovoi-otchet.html', data)
 
def structura_page(request):
    return render(request, 'web/struktura.html')

def zakup_page(request):
    data = {
        'purchases' : map(
            mapping_purchase_description,
            map(
                mapping_purchase_creation_date,
                Purchase.objects.all()
            )
        )
    }
    return render(request, 'web/zakup.html', data)

def zakup_itogi_page(request):
    data = {
        'results' : map(
            mapping_purchase_description,
            map(
                mapping_purchase_creation_date,
                Results.objects.all()
            )
        )
    }
    return render(request, 'web/zakup-itogi.html', data)

def result_page(request, pk):
    data = {
        'result': mapping_news_creation_date(Results.objects.get(pk=pk))
    }
    return render(request, 'web/result_page.html', data)

def gm_page(request, pk):
    data = {
        'gm' : Government.objects.get(pk=pk)
    }
    return render(request, 'web/government-member.html', data)

def zakup_main_page(request):
    return render(request, 'web/zakup-main.html')

def news_page(request):
    lang = request.get_full_path()[1:3]
    data = {
        'news_list' : map(
            mapping_news_creation_date,
            map(
                mapping_title, 
                News.objects.filter(
                    title_en__isnull=False, description_en__isnull=False
                ).order_by('-creation_date') if lang == 'en' else 
                    (News.objects.filter(
                    title_kk__isnull=False, description_kk__isnull=False
                ).order_by('-creation_date') if lang == 'kk' else 
                News.objects.all().order_by('-creation_date'))
            )
        )
    }
    
    return render(request, 'web/news-page.html', data)

def contact_page(request):
    return render(request, 'web/contact.html')

def purchase_page(request, pk):
    data = {
        'purchase' : mapping_news_creation_date(increase_visits(Purchase.objects.get(pk=pk)))
    }
    return render(request, 'web/purchase-page.html', data)

def step_2_page(request):
    return render(request, 'web/step2.html')

def step_3_page(request):
    return render(request, 'web/step3.html')

def build_page(request):
    return render(request, 'web/build-page.html')
    
def bp_rek_page(request):
    return render(request, 'web/bp-rek.html')

def page_404(request, ex=None):
    return render(request, 'web/404page.html')

def google_page(request):
    return render(request, 'web/google29157018848abf4e.html')

def old_fpl_page(request):
    return render(request, 'web/oldfpl_ru.html')

def old_zakup_page(request):
    return render(request, 'web/oldzakup.html')

def new_page(request):
    return render(request, 'web/new_page.html')

def analitics_page(request):
    return render(request, 'web/analitics.html')