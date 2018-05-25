# coding -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^config/$', views.choose_service), # Выберите отчет
    url(r'^service_file/$', views.service_file), # форма для загрузки файла на сервер
    url(r'^service_file_loading/$', views.service_file_loading), # загрузка файла на сервер
    url(r'^service_electric/$', views.service_electric), # электрика, загрузка нужных полей
    url(r'^service_electric_load/$', views.service_electric_load), # электрика прогрузка
    url(r'^load_tcp_ip/$', views.load_port), # загрузка портов по элетрике
    url(r'^make_sheet/$', views.MakeSheet), #возвращает список страниц в книге excel
    url(r'^load_electric_objects/$', views.load_electric_objects), # загрузка объектов и абонентов
    url(r'^load_electric_counters/$', views.load_electric_counters), # загрузка счётчиков
#    url(r'^electric/$', views.electric),
    url(r'^service_water/$', views.service_water), # электрика, загрузка нужных полей
    url(r'^load_water_objects/$', views.load_water_objects), # вода, загрузка нужных полей
    url(r'^load_water_pulsar/$', views.load_water_pulsar), # вода, загрузка пульсаров и создание связей с абонентами
    url(r'^load_water_port/$', views.load_water_port), # загрузка портов из файла для воды
    
    url(r'^service_change_electric/$', views.change_electric_meters), # замена одного счётчика на другой
    url(r'^service_replace_electric/$', views.replace_electric_meters), # поменять местами счётчики
    url(r'^service_get_info/$', views.get_info), # поменять местами счётчики
    url(r'^get_electric_progruz/$', views.replace_electric_meters), # прогрузочная ведомость в эксель
    url(r'^get_water_progruz/$', views.replace_electric_meters), # прогрузочная ведомость в эксель
    url(r'^get_heat_progruz/$', views.replace_electric_meters), # прогрузочная ведомость в эксель
    url(r'^load_balance_group/$', views.load_balance_group), # загрузка портов по элетрике
    url(r'^service_balance_load/$', views.service_balance_load), #загрузка формы для прогурзки балансных групп
)
