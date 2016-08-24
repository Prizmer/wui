# coding -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.default),
    url(r'^tree_data/$', views.tree_data_json),
    url(r'^get_object_title/$', views.get_object_title),
    url(r'^get_object_key/$', views.get_object_key),
    url(r'^get_data_table/$', views.get_data_table),
    url(r'^export_excel_electric/$', views.export_excel_electric),
    url(r'^electric/$', views.electric),
    url(r'^economic/$', views.economic),
    url(r'^water/$', views.water),
    url(r'^heat/$', views.heat),
    url(r'^gas/$', views.gas),




    # Отчеты. Чётные - один календарь. Нечётные - два календаря.
    url(r'^0/$', views.choose_report), # Выберите отчет
    url(r'^1/$', views.data_table_3_tarifa_k), # Потребление за период по T0 A+ и T0 R+ с учётом коэфф.
    url(r'^2/$', views.report_2), # Простой отчёт
    url(r'^3/$', views.data_table_period_3_tarifa), # показания за период. 3 тарифа
    url(r'^4/$', views.profil_30_aplus), #получасовки
    url(r'^6/$', views.hour_increment), #часовые приращения энергии
    url(r'^7/$', views.economic_electric), #удельный расход электроэнергии
    url(r'^8/$', views.rejim_day), #режимный день
    url(r'^10/$', views.pokazaniya_water), # показания по воде
    url(r'^11/$', views.potreblenie_water), # потребление по воде
    url(r'^12/$', views.pokazaniya_water_identificators), # потребление по воде с идентификаторами
    url(r'^14/$', views.electric_simple_2_zones), # Показания по электричеству на дату. 2 тарифа
    url(r'^16/$', views.electric_simple_3_zones_v2), # Показания по электричеству на дату. 3 тарифа
    url(r'^17/$', views.electric_potreblenie_3_zones_v2), # Потребление по электричеству за период. 3 тарифа
    url(r'^18/$', views.pokazaniya_heat), # показания по теплу
    url(r'^19/$', views.potreblenie_heat), # потребление по теплу
    url(r'^20/$', views.pokazaniya_heat_current), # текущие показания по теплу

    url(r'^22/$', views.pokazaniya_spg), #показания суточные по СПГ
    url(r'^23/$', views.test_test),



    

   
   #---- Test urls
    url(r'^addnum/$', views.add_numbers),

   

)
