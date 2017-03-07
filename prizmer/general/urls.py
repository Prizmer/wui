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
    url(r'^1/$', views.data_table_3_tarifa_k), # Потребление за период по T0 A+ и T0 R+ с учётом коэфф.-не переделывала
    url(r'^2/$', views.report_2), # Простой отчёт-не переделывала
    url(r'^3/$', views.data_table_period_3_tarifa), # показания за период. 3 тарифа-не переделывала

    url(r'^4/$', views.profil_30_aplus), #получасовки-не переделывала
    url(r'^6/$', views.hour_increment), #часовые приращения энергии-не переделывала
    url(r'^7/$', views.economic_electric), #удельный расход электроэнергии-не переделывала
    url(r'^8/$', views.rejim_day), #режимный день-не переделывала
    url(r'^9/$', views.resources_all), #для ФилиГрад, отчёт по всем ресурсам за период
    url(r'^10/$', views.pokazaniya_water), # показания по воде-не переделывала
    url(r'^11/$', views.potreblenie_water), # потребление по воде-не переделывала
    url(r'^12/$', views.pokazaniya_water_identificators), # потребление по воде с идентификаторами-не переделывала
    url(r'^26/$', views.pokazaniya_water_gvs_hvs_current), # показания по ГВС и ХВС последние считанные 
    url(r'^28/$', views.pokazaniya_water_gvs_hvs_daily), # показания по ГВС и ХВС
    
    url(r'^24/$', views.load_balance_groups), # прогрузка балансных групп

    url(r'^14/$', views.electric_simple_2_zones_v2), # Показания по электричеству на дату. 2 тарифа
    url(r'^16/$', views.electric_simple_3_zones_v2), # Показания по электричеству на дату. 3 тарифа
    url(r'^17/$', views.electric_potreblenie_3_zones_v2), # Потребление по электричеству за период. 3 тарифа
    
    url(r'^18/$', views.pokazaniya_heat_v2), # показания по теплу
    url(r'^19/$', views.potreblenie_heat_v2), # потребление по теплу
    url(r'^20/$', views.pokazaniya_heat_current_v2), # текущие показания по теплу

    url(r'^22/$', views.pokazaniya_spg), #показания суточные по СПГ
    url(r'^23/$', views.test_test),

    url(r'^25/$', views.electric_between), #срез показаний С date_start ПО date_end
    url(r'^27/$', views.electric_between_2_zones), #срез показаний С date_start ПО date_end
    url(r'^29/$', views.electric_between_3_zones), #срез показаний С date_start ПО date_end
    url(r'^30/$', views.pokazaniya_sayany_v2), #показания по теплосчётчикам Саяны
    
    url(r'^31/$', views.electric_potreblenie_2_zones_v2), # Потребление по электричеству за период. 3 тарифа
    
    url(r'^32/$', views.pokazaniya_sayany_last), #показания по теплосчётчикам Саяны последние считанные от требуемой даты
    url(r'^33/$', views.heat_potreblenie_sayany), #потребление по теплосчётчикам Саяны за период
    
    url(r'^34/$', views.pokazaniya_water_hvs_tekon), # показания по ХВС -Текон
    url(r'^35/$', views.water_potreblenie_hvs_tekon), # потребление по ХВС -Текон за период
    url(r'^36/$', views.pokazaniya_water_gvs_tekon), # показания по ХВС -Текон
    url(r'^37/$', views.water_potreblenie_gvs_tekon), # потребление по ХВС -Текон за период
    
    url(r'^38/$', views.water_by_date), # вода, показания на дату
   #---- Test urls
    url(r'^addnum/$', views.add_numbers),

   

)
