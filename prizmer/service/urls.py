# coding -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^test/$', views.choose_service), # Выберите отчет
    url(r'^service_file/$', views.service_file), # форма для загрузки файла на сервер
    url(r'^service_file_loading/$', views.service_file_loading), # загрузка файла на сервер
    url(r'^service_electric/$', views.service_electric), # электрика, загрузка нужных полей
    url(r'^service_electric_load/$', views.service_electric_load), # электрика прогрузка
    url(r'^load_tcp_ip/$', views.load_port), # загрузка портов
    url(r'^make_sheet/$', views.MakeSheet), #возвращает список страниц в книге excel
    url(r'^load_electric_objects/$', views.load_electric_objects), # загрузка объектов и абонентов
    url(r'^load_electric_counters/$', views.load_electric_counters), # загрузка счётчиков
#    url(r'^electric/$', views.electric),
    url(r'^service_water/$', views.service_water), # электрика, загрузка нужных полей
    url(r'^load_water_objects/$', views.load_water_objects), # вода, загрузка нужных полей
    url(r'^load_water_pulsar/$', views.load_water_pulsar), # вода, загрузка пульсаров и создание связей с абонентами
    
)
