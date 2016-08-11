# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^1/$', views.report_3_tarifa_k),
    url(r'^2/$', views.pokazania),
    url(r'^3/$', views.pokazania_period),
    url(r'^4/$', views.profil_30_min),
    url(r'^6/$', views.report_hour_increment),
    url(r'^7/$', views.report_economic_electric),
    url(r'^8/$', views.report_rejim_day),
    url(r'^12/$', views.report_pokazaniya_water_identificators),
    url(r'^14/$', views.report_electric_simple_2_zones), # Электрика. Простой отчет по показаниям на дату. 2 Тарифа
    url(r'^16/$', views.report_electric_simple_3_zones), # Электрика. Простой отчет по показаниям на дату. 3 Тарифа
    url(r'^15/$', views.report_electric_potreblenie_2_zones), # Электрика. Отчет по потреблению за период по двум датам. 2 Тарифа.
    url(r'^17/$', views.report_electric_potreblenie_3_zones), # Электрика. Отчет по потреблению за период по двум датам. 3 Тарифа.
    url(r'^18/$', views.pokazaniya_heat_report), # Тепло. Простой отчет по показаниям на дату.
    url(r'^19/$', views.report_potreblenie_heat), # Тепло. Отчет по потреблению за период.
    url(r'^20/$', views.pokazaniya_heat_current_report), # Тепло. Простой отчет по показаниям. Последние считанные данные.
   
   
   
   
    #---- Test urls

#    url(r'^test/$', views.test_page),

)
