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
    url(r'^9/$', views.report_resources_all),
    url(r'^12/$', views.report_pokazaniya_water_identificators),
    url(r'^14/$', views.report_electric_simple_2_zones_v2), # Электрика. Простой отчет по показаниям на дату. 2 Тарифа
    url(r'^16/$', views.report_electric_simple_3_zones_v2), # Электрика. Простой отчет по показаниям на дату. 3 Тарифа
    url(r'^15/$', views.report_electric_potreblenie_2_zones), # Электрика. Отчет по потреблению за период по двум датам. 2 Тарифа.
    url(r'^17/$', views.report_electric_potreblenie_3_zones_v2), # Электрика. Отчет по потреблению за период по двум датам. 3 Тарифа.

    url(r'^18/$', views.pokazaniya_heat_report_v2), # Тепло. Простой отчет по показаниям на дату.
    url(r'^19/$', views.report_potreblenie_heat_v2), # Тепло. Отчет по потреблению за период.
    url(r'^20/$', views.pokazaniya_heat_current_report_v2), # Тепло. Простой отчет по показаниям. Последние считанные данные.
    url(r'^25/$', views.electric_between_report), # Электрика, показания на даты С date_start ПО date_end
    url(r'^27/$', views.electric_between_2_zones_report), # Электрика, показания на даты С date_start ПО date_end
    url(r'^29/$', views.electric_between_3_zones_report), # Электрика, показания на даты С date_start ПО date_end
    url(r'^26/$', views.pokazaniya_water_current_report),#текущие(последние считанные) показания для Эльфов ГВС и ХВС
    url(r'^28/$', views.pokazaniya_water_daily_report),# показания на дату  для Эльфов ГВС и ХВС
    url(r'^30/$', views.report_pokazaniya_sayany), # показания на дату. Тепло. Саяны
#    url(r'^30_arch/$', views.report_pokazaniya_sayany_archive),
   
    url(r'^31/$', views.report_electric_potreblenie_2_zones_v2), # Электрика. Отчет по потреблению за период по двум датам. 2 Тарифа.
    
    url(r'^32/$', views.report_sayany_last), #показания по теплосчётчикам Саяны последние считанные от требуемой даты
    url(r'^33/$', views.report_heat_potreblenie_sayany), # расход по теплосчётчикам Саяны по двум датам
    
    url(r'^34/$', views.report_water_tekon_hvs), # показжания на дату по теплосчётчикам Текон-хвс
    url(r'^35/$', views.report_water_potreblenie_tekon_hvs), # расход по теплосчётчикам Текон-хвс по двум датам
    url(r'^36/$', views.report_water_tekon_gvs), # показжания на дату по теплосчётчикам Текон-гвс
    url(r'^37/$', views.report_water_potreblenie_tekon_gvs), # расход по теплосчётчикам Текон-гвс по двум датам
    #---- Test urls

#    url(r'^test/$', views.test_page),

)
