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
    url(r'^comment/$', views.comment),
    url(r'^add_comment/$', views.add_comment),
    url(r'^load_comment/$', views.load_comment),
    url(r'^instruction_user/$', views.instruction_user),
    url(r'^instruction_admin/$', views.instruction_admin),



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
    url(r'^39/$', views.water_potreblenie_pulsar), # вода, показания за период Импульсные 
    
    url(r'^40/$', views.electric_check_factory_numbers), # Сверка заводских номеров приборов
    url(r'^41/$', views.forma_80020), # Отчёт по форме 80020
    
    url(r'^42/$', views.resources_all_by_date), # Отчёт по всем ресурсам на дату
    url(r'^44/$', views.resources_electric_by_date), # Отчёт по электрике
    url(r'^46/$', views.resources_water_by_date), # Отчёт по воде
    url(r'^48/$', views.resources_heat_by_date_2), # Отчёт по теплу за последнюю дату для бухгалтерии
    
    url(r'^50/$', views.tekon_heat_by_date), # показания по теплу -Текон 
    url(r'^51/$', views.tekon_heat_potreblenie), # потребление по теплу -Текон 
    
    url(r'^52/$', views.water_elf_hvs_by_date), # показания по хвс -Эльф 
    url(r'^53/$', views.water_elf_hvs_potreblenie), # потребление по хвс -Эльф 
    url(r'^54/$', views.water_elf_gvs_by_date), # показания по гвс -Эльф 
    url(r'^55/$', views.water_elf_gvs_potreblenie), # потребление по гвс -Эльф

    url(r'^56/$', views.pulsar_heat_daily), # Показание на дату с теплосчётчиков Пульсар
    url(r'^59/$', views.pulsar_heat_period), # Показание на дату с теплосчётчиков Пульсар
    url(r'^62/$', views.pulsar_heat_daily_2), # Показание на дату с теплосчётчиков Пульсар
    url(r'^61/$', views.pulsar_heat_period_2), # Показание на дату с теплосчётчиков Пульсар
    
    url(r'^57/$', views.pulsar_water_period), # Показание за период с водосчётчиков Пульсар
    url(r'^58/$', views.pulsar_water_daily), # Показание на дату с водосчётчиков Пульсар
    
    url(r'^60/$', views.pulsar_water_daily_row), # Показания по стоякам в одну строку на дату с водосчётчиков Пульсар  
    
    url(r'^63/$', views.heat_elf_period), # Показание за период Эльф-тепло
    url(r'^64/$', views.heat_elf_daily), # Показание на дату Эльф-тепло 
    
    url(r'^66/$', views.heat_water_elf_daily), # Показание на дату по Эльф-тепло и вода
    
    url(r'^67/$', views.water_pulsar_potreblenie_skladochnaya),#67. Складочная. Потребление ХВС, ГВС (с водосчётчика Пульсар)
    
    url(r'^68/$', views.rejim_day), #режимный день
    
    url(r'^69/$', views.electric_daily_graphic), #график потребления электроэнергии по дням
    url(r'^71/$', views.electric_potreblenie_3_zones_v3), # отчёт 17, но с графиком!! Потребление по электричеству за период. 3 тарифа
    url(r'^72/$', views.electric_simple_3_zones_v3), # Показания по электричеству на дату. 3 тарифа
    url(r'^73/$', views.pulsar_water_period_2), # отчёт 57, но с графиком!  Показание за период с водосчётчиков Пульсар
    #url(r'^74/$', views.electric_current_3_zones_v2), # Показания текущие для М-200 по электричеству на дату. 3 тарифа
    
    url(r'^74/$', views.heat_karat_daily),
    url(r'^75/$', views.heat_karat_potreblenie),

    url(r'^76/$', views.all_res_by_date), 
    url(r'^77/$', views.balance_period_electric),

    url(r'^79/$', views.water_potreblenie_pulsar_with_graphic), # вода, показания за период Импульсные, отчёт как 39
    
    url(r'^83/$', views.water_elf_potreblenie_monthly_with_delta), # Потребление по месяцам с эльфов хв и гв
    url(r'^84/$', views.water_elf_daily), # 
    url(r'^85/$', views.water_elf_potreblenie), # Потребление за период с эльфов хв и гв
    
    url(r'^81/$', views.pulsar_heat_period_with_graphic), # Показание на дату с теплосчётчиков Пульсар, отчёт как 59
    
    url(r'^86/$', views.electric_res_status),
    url(r'^88/$', views.heat_digital_res_status),
    url(r'^90/$', views.water_impulse_res_status),
    
    url(r'^92/$', views.electric_res_status_monthly),

    url(r'^87/$', views.balance_period_water_impulse),
    
   #---- Test urls
    url(r'^addnum/$', views.add_numbers),

   

)
