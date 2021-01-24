 # -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, re_path
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf.urls import include, handler404, handler500
from django.conf import settings
from web.views import (
    index, actives_page, active_page, ofond_page, 
    main_info_page, org_struktura_page, strateg_napr_page, 
    rukovodstvo2_page, sostav_pravlenia_page, comitet_func_page,
    riski_page, kodeks_page, principi_page, build_page_divi_page,
    build_page_razv_page, akti_page, godovoi_otchet_page, audit_page,
    structura_page, zakup_page, news_page, contact_page, purchase_page,
    step_2_page, step_3_page, build_page, bp_rek_page, zakup_main_page,
    zakup_itogi_page, result_page, news_item_page, page_404, search_page, new_page,
    sitemap_page, google_page, old_fpl_page, old_zakup_page, gm_page, dir_page, inf_page, analitics_page
)
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^redactor/', include('redactor.urls')),
    path('redactor/', include('redactor.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('robots.txt', lambda x: HttpResponse("User-Agent: *\nAllow: /\nDisallow: /admin", content_type='text/plain')),
    path('sitemap.xml', sitemap_page),
    path('ru/sitemap.xml', sitemap_page),
    path('ru/google29157018848abf4e.html', google_page)
] 

urlpatterns += i18n_patterns(
    path('', index),
    path('search-page', search_page),
    path('active-page', actives_page),
    path('asset/<int:pk>/', active_page),
    path('ofond', ofond_page),
    path('infographics', inf_page),
    path('org-struktura', org_struktura_page),
    path('main-info', main_info_page),
    path('strateg-napr', strateg_napr_page),
    path('rukovodstvo2', rukovodstvo2_page),
    path('sostav-pravlenia', sostav_pravlenia_page),
    path('comitet-func', comitet_func_page),
    path('riski', riski_page),
    path('kodeks', kodeks_page),
    path('principi', principi_page),
    path('build-page-divi', build_page_divi_page),
    path('build-page-razv', build_page_razv_page),
    path('akti', akti_page),
    path('audit', audit_page),
    path('godovoi-otchet', godovoi_otchet_page),
    path('struktura', structura_page),
    path('zakup', zakup_page),
    path('news-page', news_page),
    path('contact', contact_page),
    path('purchase/<int:pk>/', purchase_page),
    path('result/<int:pk>/', result_page),
    path('news/<int:pk>/', news_item_page),
    path('government/<int:pk>/', gm_page),
    path('director/<int:pk>/', dir_page),
    path('step2', step_2_page),
    path('step3', step_3_page),
    path('build-page', build_page),
    path('bp-rek', bp_rek_page),
    path('zakup-main', zakup_main_page),
    path('zakupki-itogi', zakup_itogi_page),
    path('404', page_404), 
    path('oldfpl', old_fpl_page), 
    path('oldzakup', old_zakup_page),
    path('new_page', new_page),
    path('analitics', analitics_page)
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
