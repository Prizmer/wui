# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:01:37 2016
Общие ф-ции из general и AskueReport
@author: Елена
"""
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, HttpResponse
from django.core.context_processors import csrf
import simplejson as json
from django.db.models import Max
from django.db import connection
import re
from excel_response import ExcelResponse
import datetime
#---------
import calendar


def daterange(start, stop, step=datetime.timedelta(days=1), inclusive=True):
    # inclusive=False to behave like range by default
    if step.days > 0:
        while start < stop:
            yield start
            start = start + step
    elif step.days < 0:
        while start > stop:
            yield start
            start = start + step
    if inclusive and start == stop:
        yield start

def get_data_table_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, type_of_meter ):
    """Функция для получения одного параметра по теплу с указанием типа прибора. Более общий вариант"""
    cursor = connection.cursor()
    cursor.execute("""SELECT 
                          daily_values.date, 
                          objects.name, 
                          abonents.name, 
                          meters.factory_number_manual, 
                          daily_values.value
                        FROM 
                          public.abonents, 
                          public.objects, 
                          public.daily_values, 
                          public.taken_params, 
                          public.link_abonents_taken_params, 
                          public.names_params, 
                          public.params, 
                          public.meters, 
                          public.types_meters
                        WHERE 
                          daily_values.id_taken_params = taken_params.id AND
                          taken_params.guid_params = params.guid AND
                          taken_params.guid_meters = meters.guid AND
                          link_abonents_taken_params.guid_abonents = abonents.guid AND
                          link_abonents_taken_params.guid_taken_params = taken_params.guid AND
                          params.guid_names_params = names_params.guid AND
                          types_meters.guid = meters.guid_types_meters AND
                          abonents.name = %s AND 
                          objects.name = %s AND 
                          names_params.name = %s AND 
                          daily_values.date = %s AND 
                          types_meters.name LIKE %s 
                        ORDER BY
                        objects.name ASC
                        LIMIT 1;""",[obj_title, obj_parent_title, my_parametr, electric_data, type_of_meter])
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, type_of_meter ):
    """Функция для получения одного параметра по теплу с указанием типа прибора"""
    cursor = connection.cursor()
    cursor.execute("""SELECT 
                      daily_values.date,
                      objects.name, 
                      abonents.name, 
                      meters.factory_number_manual, 
                      daily_values.value
                    FROM 
                      public.taken_params, 
                      public.meters, 
                      public.abonents, 
                      public.objects, 
                      public.daily_values, 
                      public.link_abonents_taken_params, 
                      public.names_params, 
                      public.params, 
                      public.types_meters
                    WHERE 
                      taken_params.guid_meters = meters.guid AND
                      meters.guid_types_meters = types_meters.guid AND
                      abonents.guid_objects = objects.guid AND
                      daily_values.id_taken_params = taken_params.id AND
                      link_abonents_taken_params.guid_abonents = abonents.guid AND
                      link_abonents_taken_params.guid_taken_params = taken_params.guid AND
                      params.guid = taken_params.guid_params AND
                      params.guid_names_params = names_params.guid AND
                      abonents.name = %s AND
                      objects.name = %s AND
                      names_params.name = %s AND
                      daily_values.date = %s AND  
                      types_meters.name = %s
                    ORDER BY
                      objects.name ASC
                    LIMIT 1;""",[obj_title, obj_parent_title, my_parametr, electric_data, type_of_meter])
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

#Отчет по теплу на начало суток
def get_data_table_by_date_heat(obj_title, obj_parent_title, electric_data):
    data_table = []
    
    my_parametr = "Энергия"    
    data_table_heat_energy      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Эльф 1.08")
    
    my_parametr = 'Объем'               
    data_table_heat_water_delta      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Эльф 1.08")

    my_parametr = 'ElfTon'               
    data_table_heat_time_on      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Эльф 1.08")

              
    for x in range(len(data_table_heat_energy)):
        data_table_temp = []
        try:
            data_table_temp.append(data_table_heat_energy[x][0]) # дата
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_energy[x][2]) # имя абонента
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_energy[x][3]) # заводской номер
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_energy[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_water_delta[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_time_on[x][4]) # время работы
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")

        data_table.append(data_table_temp)
    return data_table

#------------

def makeSqlQuery_heat_parametr_for_period_for_abon_daily(obj_title, obj_parent_title , electric_data_start,electric_data_end,my_params):
    sQuery="""
select z1.ab_name, z1.ab_name, z1.factory_number_manual,z1.energy, z2.energy, z2.energy-z1.energy as delta
from
(SELECT 
daily_values.date,   
 objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          daily_values.value as energy                   
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  abonents.name = '%s' AND 
  objects.name = '%s' AND 
  daily_values.date= '%s' and
  names_params.name='%s'
  order by  daily_values.value ASC
  Limit 1) z1,
  (SELECT 
daily_values.date,   
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual, 
                          daily_values.value as energy

FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  abonents.name = '%s' AND 
  objects.name = '%s' AND 
  daily_values.date= '%s' and
  names_params.name='%s'
  order by  daily_values.value ASC
  Limit 1) z2
  where z1.ab_name=z2.ab_name;"""%(obj_title, obj_parent_title , electric_data_start,my_params[0],obj_title, obj_parent_title ,electric_data_end,my_params[0])
    return sQuery

def get_data_table_heat_parametr_for_period_for_abon_v2(obj_title, obj_parent_title, electric_data_start,electric_data_end, my_params):
    cursor = connection.cursor()
    cursor.execute(makeSqlQuery_heat_parametr_for_period_for_abon_daily(obj_title, obj_parent_title , electric_data_start,electric_data_end,my_params))
    data_table = cursor.fetchall()
    return data_table

def makeSqlQuery_heat_by_date_daily_for_abon(obj_title, obj_parent_title, electric_data_end,my_params):
    sQuery="""SELECT abonents.name,
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = '%s' then daily_values.value else null end) as energy,
                          sum(Case when names_params.name = '%s' then daily_values.value else null end) as volume,
                          sum(Case when names_params.name = '%s' then daily_values.value else null end) as elfTon                                
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  abonents.name = '%s' AND 
  objects.name = '%s' AND 
  daily_values.date= '%s' AND 
  types_meters.name = '%s'
  group by   abonents.name, meters.factory_number_manual;"""%(my_params[0],my_params[1],my_params[2],obj_title, obj_parent_title, electric_data_end,my_params[3])
    return sQuery

def makeSqlQuery_heat_by_date_daily_for_obj(obj_title, electric_data_end,my_params):
    sQuery="""
    select heat_abons.ab_name, heat_abons.ab_name, heat_abons.factory_number_manual, z1.energy, z1.volume,z1.elfTon
from heat_abons
left join
(SELECT 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = '%s' then daily_values.value else null end) as energy,
                          sum(Case when names_params.name = '%s' then daily_values.value else null end) as volume,
                          sum(Case when names_params.name = '%s' then daily_values.value else null end) as elfTon                                
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  objects.name = '%s' AND 
  daily_values.date= '%s' AND 
  types_meters.name = '%s'
  group by   abonents.name, meters.factory_number_manual
  ) z1
on heat_abons.ab_name=z1.ab_name
where heat_abons.obj_name='%s'
order by heat_abons.ab_name"""%(my_params[0],my_params[1],my_params[2],obj_title, electric_data_end,my_params[3],obj_title)
    return sQuery

def get_data_table_heat_parametr_by_date_daily_v2(obj_title, obj_parent_title,electric_data_end, my_params, isAbon):
    cursor = connection.cursor()
    if isAbon:
        cursor.execute(makeSqlQuery_heat_by_date_daily_for_abon(obj_title, obj_parent_title, electric_data_end,my_params))
    else:
        cursor.execute(makeSqlQuery_heat_by_date_daily_for_obj(obj_title, electric_data_end,my_params))
    data_table = cursor.fetchall()
    return data_table

def makeSqlQuery_heat_parametr_for_period(obj_title, electric_data_start,electric_data_end,my_params):
    sQuery="""
    Select heat_abons.ab_name,heat_abons.ab_name,heat_abons.factory_number_manual, z3.energy, z3.energy2, z3.delta
from heat_abons
left join 
(select z1.ab_name, z1.factory_number_manual,z1.energy, z2.energy as energy2, z2.energy-z1.energy as delta
from
(SELECT 
daily_values.date,   
                        
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          daily_values.value as energy                   
                                                    
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND

  objects.name = '%s' AND 
  daily_values.date= '%s' and
  names_params.name='%s'
  order by  daily_values.value ASC
  ) z1,
  (SELECT 
daily_values.date,   
                        
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          daily_values.value as energy                   
                                                    
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND

  objects.name = '%s' AND 
  daily_values.date= '%s' and
  names_params.name='%s'
  order by  daily_values.value ASC
  ) z2
  where z1.ab_name=z2.ab_name) z3
  on heat_abons.ab_name=z3.ab_name
  where heat_abons.obj_name='%s'
  order by heat_abons.ab_name
    """%(obj_title, electric_data_start,my_params[0],obj_title,electric_data_end,my_params[0],obj_title)
    #print sQuery
    return sQuery

def get_data_table_heat_parametr_for_period_v2(obj_title, electric_data_start,electric_data_end, my_params):
    cursor = connection.cursor()
    cursor.execute(makeSqlQuery_heat_parametr_for_period(obj_title, electric_data_start,electric_data_end,my_params))
    data_table = cursor.fetchall()
    return data_table

def get_data_table_by_date_heat_v2(obj_title, obj_parent_title, electric_data_end, isAbon):
    data_table = []
    my_parametr = [u'Энергия',u'Объем',u'ElfTon',u'Эльф 1.08']
    data_table= get_data_table_heat_parametr_by_date_daily_v2(obj_title, obj_parent_title,electric_data_end, my_parametr, isAbon)
    if len(data_table)>0: data_table=ChangeNull(data_table, None)
    return data_table

def get_data_table_for_period_for_abon_heat_v2(obj_title, obj_parent_title, electric_data_start, electric_data_end):
    data_table = []
    my_parametr = [u'Энергия'] #если будут проблемы,то возможно передлать в sql выборку на Эльф 1.08
    data_table= get_data_table_heat_parametr_for_period_for_abon_v2(obj_title, obj_parent_title, electric_data_start,electric_data_end, my_parametr)
    if len(data_table)>0: data_table=ChangeNull(data_table, None)
    return data_table

def get_data_table_for_period_heat_v2(obj_title, obj_parent_title, electric_data_start, electric_data_end):
    data_table = []
    my_parametr = [u'Энергия']#если будут проблемы,то возможно передлать в sql выборку на Эльф 1.08
    data_table= get_data_table_heat_parametr_for_period_v2(obj_title, electric_data_start,electric_data_end, my_parametr)
    if len(data_table)>0: data_table=ChangeNull(data_table, None)
    return data_table

def get_data_table_heat_parametr_current(obj_title, obj_parent_title, my_parametr, type_of_meter ):
    """Функция для получения одного параметра по теплу с указанием типа прибора"""
    cursor = connection.cursor()
    cursor.execute("""SELECT 
                          current_values.date,
                          current_values.time, 
                          objects.name, 
                          abonents.name, 
                          meters.factory_number_manual, 
                          current_values.value
                        FROM 
                          public.abonents, 
                          public.objects, 
                          public.current_values, 
                          public.taken_params, 
                          public.link_abonents_taken_params, 
                          public.names_params, 
                          public.params, 
                          public.meters, 
                          public.types_meters
                        WHERE 
                          current_values.id_taken_params = taken_params.id AND
                          taken_params.guid_params = params.guid AND
                          taken_params.guid_meters = meters.guid AND
                          link_abonents_taken_params.guid_abonents = abonents.guid AND
                          link_abonents_taken_params.guid_taken_params = taken_params.guid AND
                          params.guid_names_params = names_params.guid AND
                          types_meters.guid = meters.guid_types_meters AND
                          abonents.name = %s AND 
                          objects.name = %s AND 
                          names_params.name = %s AND 
                          types_meters.name = %s 
                        ORDER BY
                        objects.name ASC
                        LIMIT 1;""",[obj_title, obj_parent_title, my_parametr, type_of_meter])
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Время  2 - Имя объекта, 3 - Имя абонента, 4 - заводской номер, 5 - значение
    return data_table
    
def get_data_table_current_heat(obj_title, obj_parent_title):

    data_table = []
    
    my_parametr = "Энергия"    
    data_table_heat_energy_current       = get_data_table_heat_parametr_current(obj_title, obj_parent_title, my_parametr, u"Эльф 1.08")
    
    my_parametr = 'Объем'               
    data_table_heat_water_delta_current  = get_data_table_heat_parametr_current(obj_title, obj_parent_title, my_parametr, u"Эльф 1.08")

    my_parametr = 'ElfTon'               
    data_table_heat_time_on_current      = get_data_table_heat_parametr_current(obj_title, obj_parent_title, my_parametr, u"Эльф 1.08")

    my_parametr = "Ti"    
    data_table_heat_temp_in_current       = get_data_table_heat_parametr_current(obj_title, obj_parent_title, my_parametr, u"Эльф 1.08")
    
    my_parametr = 'To'               
    data_table_heat_temp_out_current  = get_data_table_heat_parametr_current(obj_title, obj_parent_title, my_parametr, u"Эльф 1.08")

    my_parametr = 'ElfErr'               
    data_table_heat_error_current      = get_data_table_heat_parametr_current(obj_title, obj_parent_title, my_parametr, u"Эльф 1.08")
              
    for x in range(len(data_table_heat_energy_current)):
        data_table_temp = []
        try:
            data_table_temp.append(data_table_heat_energy_current[x][0]) # дата
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_energy_current[x][1]) # время
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_energy_current[x][3]) # имя абонента
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_energy_current[x][4]) # заводской номер
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_energy_current[x][5]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_water_delta_current[x][5]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_time_on_current[x][5]) # время работы
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_temp_in_current[x][5]) # значение температуры входа
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_temp_out_current[x][5]) # значение температуры выхода
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_temp_in_current[x][5] - data_table_heat_temp_out_current[x][5]) # значение температуры выхода
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_error_current[x][5]) # код ошибки
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        data_table.append(data_table_temp)
    return data_table
    

def makeSqlQuery_heat_parametr_current(obj_title, obj_parent_title ,params, res):

    sQuery="""
Select z1.date,  z2.time_ask, z1.ab_name, z1.factory_number_manual,z1.energy, z1.volume, z1.elfTon, z1.ti,z1.t0, z1.t0-z1.ti as deltaT ,z1.elfErr
From
(SELECT 
current_values.date,                           
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as energy,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as volume,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as elfTon,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as ti,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as t0,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as elfErr
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.current_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  current_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  abonents.name = '%s' AND 
  objects.name = '%s' AND 
  types_meters.name = '%s'
  group by current_values.date, objects.name,abonents.name, meters.factory_number_manual) z1,
  (
SELECT 
current_values.date, current_values.time as time_ask,objects.name, abonents.name, meters.factory_number_manual
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.current_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  current_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  abonents.name = '%s' AND 
  objects.name = '%s' AND 
  types_meters.name = '%s'
  order by current_values.time DESC
  Limit 1
  ) z2;"""%(params[0],params[1],params[2],params[3],params[4],params[5], obj_title, obj_parent_title , res, obj_title, obj_parent_title , res)

    return sQuery

def makeSqlQuery_heat_parametr_current_for_all(obj_title, params, res):
    sQuery="""
Select z3.date,  z3.time_ask, z4.ab_name, z3.factory_number_manual, z3.energy, z3.volume, z3.elfTon, z3.ti,z3.t0, z3.deltaT ,z3.elfErr
from
(SELECT 
  abonents.name as ab_name, 
  objects.name, 
  types_meters.name, 
  meters.factory_number_manual
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters, 
  public.types_meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  meters.guid_types_meters = types_meters.guid AND
  types_meters.name = '%s' and
  objects.name='%s'
  group by   abonents.name, 
  objects.name, 
  types_meters.name, 
  meters.factory_number_manual
  order by abonents.name ASC) z4
left join
(Select z1.date,  z2.time_ask, z1.ab_name, z1.factory_number_manual,z1.energy, z1.volume, z1.elfTon, z1.ti,z1.t0, z1.t0-z1.ti as deltaT ,z1.elfErr
From
(SELECT 
current_values.date,                           
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as energy,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as volume,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as elfTon,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as ti,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as t0,
                          sum(Case when names_params.name = '%s' then current_values.value else null end) as elfErr
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.current_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  current_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s'
  group by current_values.date, objects.name,abonents.name, meters.factory_number_manual) z1,
  (
SELECT 
current_values.date,    
current_values."time" as time_ask,                       
                          objects.name, 
                          abonents.name, 
                          meters.factory_number_manual
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.current_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  current_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s'
  order by current_values."time" DESC
  Limit 1
  ) z2
  order by ab_name ASC) z3
  on z4.ab_name=z3.ab_name
  group by z3.date, z3.time_ask, z3.ab_name, z4.ab_name, z3.factory_number_manual, z3.energy, z3.volume, z3.elfTon, z3.ti,z3.t0, z3.deltaT ,z3.elfErr
  order by z4.ab_name ASC;"""%(res, obj_title, params[0],params[1],params[2],params[3],params[4],params[5], obj_title,  res, obj_title, res)
    return sQuery

def get_data_table_heat_parametr_current_v2(obj_title, obj_parent_title, my_params, res, isAbon):
    cursor = connection.cursor()
    data_table=[]
    if isAbon:
        cursor.execute(makeSqlQuery_heat_parametr_current(obj_title, obj_parent_title ,my_params, res))
    else:
        cursor.execute(makeSqlQuery_heat_parametr_current_for_all(obj_title ,my_params, res))
    data_table = cursor.fetchall()
    return data_table

def get_data_table_current_heat_v2(obj_title, obj_parent_title, isAbon):
    data_table = []
    my_params=[u'Энергия' ,u'Объем',u'ElfTon',u'Ti',u'To',u'ElfErr']
    data_table= get_data_table_heat_parametr_current_v2(obj_title, obj_parent_title, my_params, u'Эльф 1.08', isAbon)
    date=None
    for x in data_table:
        if x[0] != None:
            date=x[0]
            break
    if len(data_table)>0:
        data_table=ChangeNull(data_table, date)
    return data_table

def get_data_table_electric_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr ):
    cursor = connection.cursor()
    cursor.execute("""SELECT 
                        daily_values.date, objects.name, abonents.name, meters.factory_number_manual, daily_values.value 
                        FROM
                         public.daily_values, public.link_abonents_taken_params, public.taken_params, public.abonents, public.objects, public.names_params, public.params, public.meters 
                        WHERE
                         taken_params.guid = link_abonents_taken_params.guid_taken_params AND taken_params.id = daily_values.id_taken_params AND taken_params.guid_params = params.guid AND taken_params.guid_meters = meters.guid AND abonents.guid = link_abonents_taken_params.guid_abonents AND objects.guid = abonents.guid_objects AND names_params.guid = params.guid_names_params AND
                        abonents.name = %s AND 
                        objects.name = %s AND 
                        names_params.name = %s AND 
                        daily_values.date = %s 
                        ORDER BY
                        objects.name ASC;""",[obj_title, obj_parent_title, my_parametr, electric_data])
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def makeSqlQuery_electric_by_daily_or_monthly_for_group(obj_title, electric_data, params, dm):
    sQuery="""select z2.monthly_date,
 z3.name_abonents, z2.number_manual,
      z3.znak*z2.t0, z3.znak*z2.t1, z3.znak*z2.t2, z3.znak*z2.t3
from 
(SELECT  
 abonents.name as name_abonents,
  (Case when link_balance_groups_meters.type = 'True' then 1 else -1 end)  as znak
FROM 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params,
  public.meters, 
  public.link_balance_groups_meters, 
  public.balance_groups,
  public.names_params,
  public.params
WHERE 
  taken_params.guid = link_abonents_taken_params.guid_taken_params AND 
  abonents.guid = link_abonents_taken_params.guid_abonents  AND 
  taken_params.guid_params = params.guid AND 
  names_params.guid = params.guid_names_params AND
  taken_params.guid_meters = meters.guid AND 
  meters.guid=link_balance_groups_meters.guid_meters AND
  balance_groups.guid=link_balance_groups_meters.guid_balance_groups AND
  balance_groups.name='%s' 
  GROUP BY abonents.name, link_balance_groups_meters.type) z3
Left join
(SELECT z1.guid,z1.monthly_date, z1.name_group, z1.name_abonents, z1.number_manual, 
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t0,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t1,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t2,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t3
FROM
                        (SELECT 
                        balance_groups.guid,
 monthly_values.date as monthly_date, 
 balance_groups.name as name_group, 
 abonents.name as name_abonents, 
 meters.factory_number_manual as number_manual, 
 monthly_values.value as value_monthly, 
 names_params.name as params_name
FROM 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params,
  public.monthly_values, 
  public.meters, 
  public.link_balance_groups_meters, 
  public.balance_groups,
  public.names_params,
  public.params
WHERE 
  taken_params.guid = link_abonents_taken_params.guid_taken_params AND 
  abonents.guid = link_abonents_taken_params.guid_abonents  AND 
  taken_params.id = monthly_values.id_taken_params AND 
  taken_params.guid_params = params.guid AND 
  names_params.guid = params.guid_names_params AND
  taken_params.guid_meters = meters.guid AND 
  meters.guid=link_balance_groups_meters.guid_meters AND
  balance_groups.guid=link_balance_groups_meters.guid_balance_groups AND
  balance_groups.name='%s' AND
  monthly_values.date = '%s') z1
group by z1.name_group, z1.monthly_date, z1.name_abonents, z1.number_manual, z1.guid
order by name_abonents ASC) z2
on z3.name_abonents=z2.name_abonents
group by z2.monthly_date,
      z2.name_group, z3.name_abonents,
      z2.number_manual, z2.t0, z2.t1, z2.t2, z2.t3, z3.znak
ORDER BY z3.name_abonents ASC;    """%(obj_title, params[0],params[1],params[2],params[3], obj_title, electric_data)

    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('monthly',dm)
        return sQuery
    else: return """Select 'Н/Д'"""

def get_data_table_electric_parametr_by_date_for_group_v2(obj_title, electric_data, params, dm):
    cursor = connection.cursor()
    #dm - строка, содержащая monthly or daily для sql-запроса или current
    cursor.execute(makeSqlQuery_electric_by_daily_or_monthly_for_group(obj_title, electric_data, params, dm))
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def makeSqlQuery_water_for_abon_gvs_hvs_daily(obj_title, obj_parent_title, electric_data, params, dm):
    sQuery="""
SELECT 
  daily_values.date,
  abonents.name, 
  meters.factory_number_manual,  
   sum(Case when names_params.name = '%s' then daily_values.value else null end) as hvs,
   sum(Case when names_params.name = '%s' then daily_values.value else null end) as gvs,
  objects.name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources, 
  public.meters, 
  public.types_meters,
  daily_values
WHERE 
daily_values.id_taken_params=taken_params.id and
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  meters.guid_types_meters = types_meters.guid and
  resources.name='%s' and
  objects.name='%s' and
  abonents.name='%s' 
  group by   objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  daily_values.date 
  order by daily_values.date ASC
  Limit 1"""%(params[0],params[1],params[2], obj_parent_title,obj_title)
    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('daily',dm)
        #print sQuery
        return sQuery
    else: return """Select 'Н/Д'"""

def makeSqlQuery_water_for_obj_gvs_hvs_daily(obj_title, obj_parent_title, electric_data, params, dm):
    sQuery="""
Select z1.date,water_abons.ab_name, water_abons.factory_number_manual, z1.hvs,z1.gvs
from water_abons
left join
(SELECT
  objects.name as obj_name, 
  abonents.name as ab_name, 
  meters.factory_number_manual,  
   sum(Case when names_params.name = '%s' then current_values.value else null end) as hvs,
   sum(Case when names_params.name = '%s' then current_values.value else null end) as gvs,
   current_values.date
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources, 
  public.meters, 
  public.types_meters,
  current_values
WHERE 
current_values.id_taken_params=taken_params.id and
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  meters.guid_types_meters = types_meters.guid and
  resources.name='%s' and
  objects.name='%s' and
  current_values.date='%s'
  group by   objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  current_values.date
  order by objects.name,  abonents.name) z1
  on water_abons.ab_name=z1.ab_name and water_abons.obj_name=z1.obj_name
  where water_abons.obj_name='%s'
  order by water_abons.ab_name

    """%(params[0],params[1],params[2], obj_title, electric_data, obj_title)
    
    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('current',dm)
        return sQuery
    else: return """Select 'Н/Д'"""

def makeSqlQuery_water_for_abon_gvs_hvs_current(obj_title, obj_parent_title, electric_data, params):
    sQuery="""
    SELECT 
    current_values.date,
   current_values.time,
  abonents.name, 
  meters.factory_number_manual,  
   sum(Case when names_params.name = '%s' then current_values.value else null end) as hvs,
   sum(Case when names_params.name = '%s' then current_values.value else null end) as gvs,    
  objects.name 
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources, 
  public.meters, 
  public.types_meters,
  current_values
WHERE 
current_values.id_taken_params=taken_params.id and
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  meters.guid_types_meters = types_meters.guid and
  resources.name='%s' and
  objects.name='%s' and
  abonents.name='%s' 
  group by   objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  current_values.date,
   current_values.time
  order by current_values.date ASC
  Limit 1;
    """%(params[0],params[1],params[2],  obj_parent_title,obj_title)

    return sQuery

def makeSqlQuery_water_for_obj_gvs_hvs_current(obj_title, obj_parent_title, electric_data, params):
    sQuery="""
Select z1.date, z1.time,water_abons.ab_name, water_abons.factory_number_manual, z1.hvs,z1.gvs, water_abons.obj_name
from water_abons
left join
(SELECT
  objects.name as obj_name, 
  abonents.name as ab_name, 
  meters.factory_number_manual,  
   sum(Case when names_params.name = '%s' then current_values.value else null end) as hvs,
   sum(Case when names_params.name = '%s' then current_values.value else null end) as gvs,
   current_values.date,
   current_values.time
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources, 
  public.meters, 
  public.types_meters,
  current_values
WHERE 
current_values.id_taken_params=taken_params.id and
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  meters.guid_types_meters = types_meters.guid and
  resources.name='%s' and
  objects.name='%s' and
  current_values.date='%s'
  group by   objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  current_values.date,
   current_values.time
  order by objects.name,  abonents.name) z1
  on water_abons.ab_name=z1.ab_name and water_abons.obj_name=z1.obj_name
  where water_abons.obj_name='%s'
  order by water_abons.ab_name

    """%(params[0],params[1],params[2], obj_title, electric_data, obj_title)
    
    return sQuery



def get_daily_water_gvs_hvs(obj_title, obj_parent_title , electric_data, dm, isAbon):
    params=[u'Канал 1',u'Канал 2', u'Импульс']
    #dm - строка, содержащая monthly or daily для sql-запроса или current
    cursor = connection.cursor()
    if isAbon:
        cursor.execute(makeSqlQuery_water_for_abon_gvs_hvs_daily(obj_title, obj_parent_title, electric_data, params, dm))
    else: 
        cursor.execute(makeSqlQuery_water_for_obj_gvs_hvs_daily(obj_title, obj_parent_title, electric_data, params, dm))
    data_table = cursor.fetchall()
    
    if len(data_table)>0: 
        if isAbon:
            data_table=ChangeNull(data_table, None)
        else:
            data_table=ChangeNull(data_table, electric_data)
    return data_table


def get_current_water_gvs_hvs(obj_title, obj_parent_title , electric_data, isAbon):
    params=[u'Канал 1',u'Канал 2', u'Импульс']
    #dm - строка, содержащая monthly or daily для sql-запроса или current
    cursor = connection.cursor()
    if isAbon:
        cursor.execute(makeSqlQuery_water_for_abon_gvs_hvs_current(obj_title, obj_parent_title, electric_data, params))
    else: 
        cursor.execute(makeSqlQuery_water_for_obj_gvs_hvs_current(obj_title, obj_parent_title, electric_data, params))
    data_table = cursor.fetchall()
    
    if len(data_table)>0: 
        if isAbon:
            data_table=ChangeNull(data_table, None)
        else:
            data_table=ChangeNull(data_table, electric_data)
    return data_table

def makeSqlQuery_electric_by_daily_or_monthly_for_object(obj_title, electric_data, params, dm, res):
    sQuery="""Select  z2.monthly_date,
   electric_abons.ab_name, 
    electric_abons.factory_number_manual, z2.t0, z2.t1, z2.t2, z2.t3,electric_abons.obj_name, z2.ktt,z2.ktn,z2.a
from electric_abons
LEFT JOIN 
(SELECT z1.monthly_date, z1.name_objects, z1.name_abonents, z1.number_manual, 
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t0,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t1,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t2,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t3,
z1.ktt,z1.ktn,z1.a

                        FROM
                        (SELECT monthly_values.date as monthly_date, 
                        objects.name as name_objects, 
                        abonents.name as name_abonents, 
                        meters.factory_number_manual as number_manual, 
                        monthly_values.value as value_monthly, 
                        names_params.name as params_name,
                        link_abonents_taken_params.coefficient as ktt,
                         link_abonents_taken_params.coefficient_2 as ktn,
                         link_abonents_taken_params.coefficient_3 as a
                        FROM
                         public.monthly_values, 
                         public.link_abonents_taken_params, 
                         public.taken_params, 
                         public.abonents, 
                         public.objects, 
                         public.names_params, 
                         public.params, 
                         public.meters,
                         public.types_meters,
                         public.resources			
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND 
                        taken_params.id = monthly_values.id_taken_params AND 
                        taken_params.guid_params = params.guid AND 
                        taken_params.guid_meters = meters.guid AND 
                        abonents.guid = link_abonents_taken_params.guid_abonents AND 
                        objects.guid = abonents.guid_objects AND 
                        names_params.guid = params.guid_names_params AND
                        params.guid_names_params=names_params.guid and 
                        types_meters.guid=meters.guid_types_meters and
                        names_params.guid_resources=resources.guid and
                        resources.name='%s' and
                 objects.name = '%s' AND                      
                        monthly_values.date = '%s' 
                        ) z1                        
                      
group by z1.name_objects, z1.monthly_date, z1.name_objects, z1.name_abonents, z1.number_manual, z1.ktt,z1.ktn,z1.a

) z2
on electric_abons.ab_name=z2.name_abonents
where electric_abons.obj_name='%s'
ORDER BY electric_abons.ab_name ASC;
"""%(params[0],params[1],params[2],params[3], res,obj_title, electric_data, obj_title)

    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('monthly',dm)
        return sQuery
    else: return """Select 'Н/Д'"""
    

def get_data_table_electric_parametr_by_date_for_object_v2(obj_title, electric_data, params, dm, res):
    cursor = connection.cursor()
    #dm - строка, содержащая monthly or daily для sql-запроса
    cursor.execute(makeSqlQuery_electric_by_daily_or_monthly_for_object(obj_title, electric_data, params, dm, res))
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def makeSqlQuery_electric_between(obj_title, obj_parent_title,data_start, data_end, params):

    sQuery="""
    Select *, 
z3.t0-lag(t0) over (order by c_date) as delta,
z3.t1-lag(t1) over (order by c_date) as delta_t1,
z3.t2-lag(t2) over (order by c_date) as delta_t2,
z3.t3-lag(t3) over (order by c_date) as delta_t3
from
(select c_date::date
from
generate_series('%s'::timestamp without time zone, '%s'::timestamp without time zone, interval '1 day') as c_date) z4
left join 
(Select  z2.daily_date,
  electric_abons.obj_name, electric_abons.ab_name, 
    electric_abons.factory_number_manual, z2.t0, z2.t1, z2.t2, z2.t3, z2.ktn, z2.ktt, z2.a 
from electric_abons
LEFT JOIN 
(SELECT z1.daily_date, z1.name_objects, z1.name_abonents, z1.number_manual, 
sum(Case when z1.params_name = '%s' then z1.value_daily  end) as t0,
sum(Case when z1.params_name = '%s' then z1.value_daily  end) as t1,
sum(Case when z1.params_name = '%s' then z1.value_daily  end) as t2,
sum(Case when z1.params_name = '%s' then z1.value_daily  end) as t3,
z1.ktn, z1.ktt, z1.a 
                        FROM
                        (SELECT daily_values.date as daily_date, 
                        objects.name as name_objects, 
                        abonents.name as name_abonents, 
                        meters.factory_number_manual as number_manual, 
                        daily_values.value as value_daily, 
                        names_params.name as params_name,
                        link_abonents_taken_params.coefficient as ktt,
                         link_abonents_taken_params.coefficient_2 as ktn,
                          link_abonents_taken_params.coefficient_3 as a
                        FROM
                         public.daily_values, 
                         public.link_abonents_taken_params, 
                         public.taken_params, 
                         public.abonents, 
                         public.objects, 
                         public.names_params, 
                         public.params, 
                         public.meters,
                         public.types_meters,
                         public.resources			
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND 
                        taken_params.id = daily_values.id_taken_params AND 
                        taken_params.guid_params = params.guid AND 
                        taken_params.guid_meters = meters.guid AND 
                        abonents.guid = link_abonents_taken_params.guid_abonents AND 
                        objects.guid = abonents.guid_objects AND 
                        names_params.guid = params.guid_names_params AND
                        params.guid_names_params=names_params.guid and 
                        types_meters.guid=meters.guid_types_meters and
                        names_params.guid_resources=resources.guid and
                        resources.name='%s' and
                        abonents.name = '%s' AND 
                        objects.name = '%s' AND                      
                        daily_values.date between '%s' and '%s'
                        ) z1                      
group by z1.name_objects, z1.daily_date, z1.name_objects, z1.name_abonents, z1.number_manual, z1.ktn, z1.ktt, z1.a 
) z2
on electric_abons.ab_name=z2.name_abonents
where electric_abons.ab_name = '%s' AND electric_abons.obj_name='%s'
ORDER BY electric_abons.ab_name, z2.daily_date  ASC) z3
on z4.c_date=z3.daily_date 
order by z4.c_date""" % (data_start,data_end,params[0],params[1],params[2],params[3],unicode(params[4]),unicode(obj_title), unicode(obj_parent_title), data_start,data_end,unicode(obj_title), unicode(obj_parent_title))

    return sQuery

def get_data_table_electric_between(obj_title, obj_parent_title,data_start, data_end):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+', u'Электричество']
    cursor = connection.cursor()
    cursor.execute(makeSqlQuery_electric_between(obj_title, obj_parent_title,data_start, data_end, params))
    data_table = cursor.fetchall()
    if len(data_table)>0: data_table=ChangeNull(data_table, None)
    return data_table


def makeSqlQuery_electric_by_daily_or_monthly(obj_title, obj_parent_title, electric_data, params, dm):
    sQuery="""
   Select  z2.daily_date,
   electric_abons.ab_name, 
   electric_abons.factory_number_manual, z2.t0, z2.t1, z2.t2, z2.t3, electric_abons.obj_name,  z2.ktt, z2.ktn, z2.a 
from electric_abons
LEFT JOIN 
(SELECT z1.daily_date, z1.name_objects, z1.name_abonents, z1.number_manual, 
sum(Case when z1.params_name = '%s' then z1.value_daily  end) as t0,
sum(Case when z1.params_name = '%s' then z1.value_daily  end) as t1,
sum(Case when z1.params_name = '%s' then z1.value_daily  end) as t2,
sum(Case when z1.params_name = '%s' then z1.value_daily  end) as t3,
z1.ktn, z1.ktt, z1.a 
                        FROM
                        (SELECT daily_values.date as daily_date, 
                        objects.name as name_objects, 
                        abonents.name as name_abonents, 
                        meters.factory_number_manual as number_manual, 
                        daily_values.value as value_daily, 
                        names_params.name as params_name,
                        link_abonents_taken_params.coefficient as ktt,
                         link_abonents_taken_params.coefficient_2 as ktn,
                          link_abonents_taken_params.coefficient_3 as a
                        FROM
                         public.daily_values, 
                         public.link_abonents_taken_params, 
                         public.taken_params, 
                         public.abonents, 
                         public.objects, 
                         public.names_params, 
                         public.params, 
                         public.meters,
                         public.types_meters,
                         public.resources
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND 
                        taken_params.id = daily_values.id_taken_params AND 
                        taken_params.guid_params = params.guid AND 
                        taken_params.guid_meters = meters.guid AND 
                        abonents.guid = link_abonents_taken_params.guid_abonents AND 
                        objects.guid = abonents.guid_objects AND 
                        names_params.guid = params.guid_names_params AND
                        params.guid_names_params=names_params.guid and 
                        types_meters.guid=meters.guid_types_meters and
                        names_params.guid_resources=resources.guid and
                        resources.name='Электричество' and
                 abonents.name = '%s' AND objects.name = '%s' AND                      
                        daily_values.date = '%s' 
                        ) z1                      
group by z1.name_objects, z1.daily_date, z1.name_objects, z1.name_abonents, z1.number_manual, z1.ktn, z1.ktt, z1.a 
) z2
on electric_abons.ab_name=z2.name_abonents
where electric_abons.ab_name = '%s' AND electric_abons.obj_name='%s'
ORDER BY electric_abons.ab_name ASC;""" % (params[0],params[1],params[2],params[3],obj_title, obj_parent_title, electric_data, obj_title,obj_parent_title )
    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('daily',dm)
        return sQuery
    else: return """Select 'Н/Д'"""
    
def get_data_table_electric_parametr_by_date_monthly_v2(obj_title, obj_parent_title, electric_data, params, dm):
    cursor = connection.cursor()
    #dm - строка, содержащая monthly or daily для sql-запроса
    cursor.execute(makeSqlQuery_electric_by_daily_or_monthly(obj_title, obj_parent_title, electric_data, params, dm))
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def makeSqlQuery_electric_by_period(obj_title, obj_parent_title, date_start, date_end, params,res, dm):
    sQuery="""
Select z3.ab_name, z3.factory_number_manual,
z3.t0_start, z3.t1_start, z3.t2_start, z3.t3_start, z3.t4_start, 
z4.t0_end, z4.t1_end, z4.t2_end, z4.t3_end, z4.t4_end,  
z4.t0_end-z3.t0_start as delta_t0, z4.t1_end-z3.t1_start as delta_t1, z4.t2_end-z3.t2_start as delta_t2, z4.t3_end-z3.t3_start as delta_t3, z4.t4_end-z3.t4_start as delta_t4,
z3.t0R_start, z4.t0R_end,  z4.t0R_end-z3.t0R_start as delta_t0R, z4.ktt,
z4.ktt*z4.ktn*(z4.t0_end-z3.t0_start), z4.ktt*z4.ktn*(z4.t0R_end-z3.t0R_start), z4.ktn, z4.a
from
(Select z2.ktt, z2.ktn, z2.a,z2.date as date_start, electric_abons.obj_name, electric_abons.ab_name, electric_abons.factory_number_manual, z2.name_res, z2.t0 as t0_end, z2.t1 as t1_end, z2.t2 as t2_end, z2.t3 as t3_end, z2.t4 as t4_end, z2.t0r as t0r_end
from electric_abons
Left join
(SELECT z1.ktt, z1.ktn,z1.a,z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t1,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t2,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t3,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t4,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0R
                        FROM
                        (
                                SELECT 
                                  link_abonents_taken_params.coefficient_2 as ktn,
                                  link_abonents_taken_params.coefficient as ktt,
                                  link_abonents_taken_params.coefficient_3 as a,
                                  daily_values.date,    
                                  daily_values.value,                            
                                  abonents.name, 
                                  daily_values.id_taken_params, 
                                  objects.name as name_objects,
                                  names_params.name as params_name,
                                  meters.factory_number_manual as num_manual, 
                                  resources.name as name_res
                                FROM 
                                  public.daily_values, 
                                  public.link_abonents_taken_params, 
                                  public.taken_params, 
                                  public.abonents, 
                                  public.objects, 
                                  public.names_params, 
                                  public.params, 
                                  public.meters, 
                                  public.resources
                                WHERE 
                                  taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                  taken_params.id = daily_values.id_taken_params AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  abonents.guid = link_abonents_taken_params.guid_abonents AND
                                  objects.guid = abonents.guid_objects AND
                                  names_params.guid = params.guid_names_params AND
                                  resources.guid = names_params.guid_resources AND                                  
                                  objects.name = '%s' AND 
                                  abonents.name='%s' and
                                  daily_values.date = '%s' AND 
                                  resources.name = '%s'
                                  ) z1                       
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res, z1.ktt, z1.ktn, z1.a
                      order by z1.name) z2
on electric_abons.ab_name=z2.name_abonent
where electric_abons.obj_name='%s') z4, 

(Select z2.date as date_start, electric_abons.obj_name, electric_abons.ab_name, electric_abons.factory_number_manual, z2.name_res, z2.t0 as t0_start, z2.t1 as t1_start, z2.t2 as t2_start, z2.t3 as t3_start, z2.t4 as t4_start, z2.t0r as t0r_start
from electric_abons
Left join
(SELECT z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t1,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t2,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t3,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t4,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0R

                        FROM
                        (
SELECT 
                                  daily_values.date,    
                                  daily_values.value,                            
                                  abonents.name, 
                                  daily_values.id_taken_params, 
                                  objects.name as name_objects,
                                  names_params.name as params_name,
                                  meters.factory_number_manual as num_manual, 
                                  resources.name as name_res
                                FROM 
                                  public.daily_values, 
                                  public.link_abonents_taken_params, 
                                  public.taken_params, 
                                  public.abonents, 
                                  public.objects, 
                                  public.names_params, 
                                  public.params, 
                                  public.meters, 
                                  public.resources
                                WHERE 
                                  taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                  taken_params.id = daily_values.id_taken_params AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  abonents.guid = link_abonents_taken_params.guid_abonents AND
                                  objects.guid = abonents.guid_objects AND
                                  names_params.guid = params.guid_names_params AND
                                  resources.guid = names_params.guid_resources AND                                  
                                  objects.name = '%s' AND 
                                  abonents.name='%s' and
                                  daily_values.date = '%s' AND 
                                  resources.name = '%s'
                                  ) z1                       
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res
                      order by z1.name) z2
on electric_abons.ab_name=z2.name_abonent
where electric_abons.obj_name='%s') z3
where z3.ab_name=z4.ab_name and z3.ab_name='%s'""" % (params[0],params[1],params[2],params[3], params[4], params[5],  obj_parent_title, obj_title, date_end, res, obj_parent_title, 
                            params[0],params[1],params[2],params[3], params[4], params[5],obj_parent_title, obj_title, date_start, res,obj_parent_title, obj_title)
    
    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('daily',dm)    
    return sQuery

def makeSqlQuery_electric_by_period_for_all(obj_title, obj_parent_title, date_start, date_end,params, res,dm):
    sQuery="""
Select z3.ab_name, z3.factory_number_manual,
z3.t0_start, z3.t1_start, z3.t2_start, z3.t3_start, z3.t4_start, 
z4.t0_end, z4.t1_end, z4.t2_end, z4.t3_end, z4.t4_end,  
z4.t0_end-z3.t0_start as delta_t0, z4.t1_end-z3.t1_start as delta_t1, z4.t2_end-z3.t2_start as delta_t2, z4.t3_end-z3.t3_start as delta_t3, z4.t4_end-z3.t4_start as delta_t4,
z3.t0R_start, z4.t0R_end,  z4.t0R_end-z3.t0R_start as delta_t0R, z4.ktt,  
z4.ktt*z4.ktn*(z4.t0_end-z3.t0_start), z4.ktt*z4.ktn*(z4.t0R_end-z3.t0R_start),z4.ktn,z4.a
from
(Select z2.ktt, z2.ktn, z2.a, z2.date as date_end, electric_abons.obj_name, electric_abons.ab_name, electric_abons.factory_number_manual, z2.name_res, z2.t0 as t0_end, z2.t1 as t1_end, z2.t2 as t2_end, z2.t3 as t3_end, z2.t4 as t4_end, z2.t0r as t0r_end
from electric_abons
Left join
(SELECT z1.ktt, z1.ktn, z1.a,z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t1,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t2,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t3,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t4,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0R

                        FROM
                        (
SELECT 
                                  link_abonents_taken_params.coefficient_2 as ktn,
                                  link_abonents_taken_params.coefficient as ktt,
                                  link_abonents_taken_params.coefficient_3 as a,
                                  daily_values.date,    
                                  daily_values.value,                            
                                  abonents.name, 
                                  daily_values.id_taken_params, 
                                  objects.name as name_objects,
                                  names_params.name as params_name,
                                  meters.factory_number_manual as num_manual, 
                                  resources.name as name_res
                                FROM 
                                  public.daily_values, 
                                  public.link_abonents_taken_params, 
                                  public.taken_params, 
                                  public.abonents, 
                                  public.objects, 
                                  public.names_params, 
                                  public.params, 
                                  public.meters, 
                                  public.resources
                                WHERE 
                                  taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                  taken_params.id = daily_values.id_taken_params AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  abonents.guid = link_abonents_taken_params.guid_abonents AND
                                  objects.guid = abonents.guid_objects AND
                                  names_params.guid = params.guid_names_params AND
                                  resources.guid = names_params.guid_resources AND                                  
                                  objects.name = '%s' AND 
                                  daily_values.date = '%s' AND 
                                  resources.name = '%s'
                                  ) z1                       
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res, z1.ktt, z1.ktn,z1.a
                      order by z1.name) z2
on electric_abons.ab_name=z2.name_abonent
where electric_abons.obj_name='%s') z4, 


(Select z2.date as date_start, electric_abons.obj_name, electric_abons.ab_name, electric_abons.factory_number_manual, z2.name_res, z2.t0 as t0_start, z2.t1 as t1_start, z2.t2 as t2_start, z2.t3 as t3_start, z2.t4 as t4_start, z2.t0r as t0r_start
from electric_abons
Left join
(SELECT z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t1,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t2,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t3,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t4,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0R

                        FROM
                        (
SELECT 
                                  daily_values.date,    
                                  daily_values.value,                            
                                  abonents.name, 
                                  daily_values.id_taken_params, 
                                  objects.name as name_objects,
                                  names_params.name as params_name,
                                  meters.factory_number_manual as num_manual, 
                                  resources.name as name_res
                                FROM 
                                  public.daily_values, 
                                  public.link_abonents_taken_params, 
                                  public.taken_params, 
                                  public.abonents, 
                                  public.objects, 
                                  public.names_params, 
                                  public.params, 
                                  public.meters, 
                                  public.resources
                                WHERE 
                                  taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                  taken_params.id = daily_values.id_taken_params AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  abonents.guid = link_abonents_taken_params.guid_abonents AND
                                  objects.guid = abonents.guid_objects AND
                                  names_params.guid = params.guid_names_params AND
                                  resources.guid = names_params.guid_resources AND                                  
                                  objects.name = '%s' AND 
                                  daily_values.date = '%s' AND 
                                  resources.name = '%s'
                                  ) z1                       
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res
                      order by z1.name) z2
on electric_abons.ab_name=z2.name_abonent
where electric_abons.obj_name='%s') z3
where z3.ab_name=z4.ab_name
order by z3.ab_name ASC""" % (params[0],params[1],params[2],params[3], params[4], params[5], obj_title, date_end, res, obj_title, 
                            params[0],params[1],params[2],params[3], params[4], params[5],obj_title,  date_start, res,obj_title)
    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('daily',dm)
    
    return sQuery

def get_data_table_electric_parametr_by_period_v2(isAbon,obj_title, obj_parent_title, electric_data_start, electric_data_end, params, res, dm):
    cursor = connection.cursor()
    #isAbon - запрос для абонента или для корпуса
    if isAbon:
        cursor.execute(makeSqlQuery_electric_by_period(obj_title, obj_parent_title, electric_data_start, electric_data_end,params, res, dm))
    else:
        cursor.execute(makeSqlQuery_electric_by_period_for_all(obj_title, obj_parent_title, electric_data_start, electric_data_end,params, res, dm))
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def makeSqlQuery_electric_by_period_for_group(obj_title, date_start, date_end,params, res):
    sQuery="""
    Select  z3.name_abonents, z3.number_manual,
z3.t0_start, z3.t1_start, z3.t2_start, z3.t3_start, z3.t4_start, 
z4.t0_end, z4.t1_end, z4.t2_end, z4.t3_end, z4.t4_end,  
z4.t0_end-z3.t0_start as delta_t0, z4.t1_end-z3.t1_start as delta_t1, z4.t2_end-z3.t2_start as delta_t2, z4.t3_end-z3.t3_start as delta_t3, z4.t4_end-z3.t4_start as delta_t4,
z3.t0R_start, z4.t0R_end,  z4.t0R_end-z3.t0R_start as delta_t0R, z4.ktt, z4.ktn, 
z4.ktt*z4.ktn*(z4.t0_end-z3.t0_start), z4.ktt*z4.ktn*(z4.t0R_end-z3.t0R_start)
from
(Select z2.group_name, z2.ktt, z2.ktn, z2.date as date_end, electric_groups.name_group, electric_groups.name_abonents, electric_groups.number_manual, z2.name_res, z2.t0 as t0_end, z2.t1 as t1_end, z2.t2 as t2_end, z2.t3 as t3_end, z2.t4 as t4_end, z2.t0r as t0r_end
from electric_groups
Left join
(SELECT z1.group_name,z1.ktt, z1.ktn, z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t1,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t2,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t3,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t4,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0R

                        FROM
                        (
SELECT 
                                  link_abonents_taken_params.coefficient_2 as ktt,
                                  link_abonents_taken_params.coefficient as ktn,
                                  daily_values.date,    
                                  daily_values.value,                            
                                  abonents.name, 
                                  daily_values.id_taken_params, 
                                  objects.name as name_objects,
                                  names_params.name as params_name,
                                  meters.factory_number_manual as num_manual, 
                                  resources.name as name_res,
                                  balance_groups.name as group_name
                                  
                                FROM 
                                  public.balance_groups,
                                  public.link_balance_groups_meters,
                                  public.daily_values, 
                                  public.link_abonents_taken_params, 
                                  public.taken_params, 
                                  public.abonents, 
                                  public.objects, 
                                  public.names_params, 
                                  public.params, 
                                  public.meters, 
                                  public.resources
                                WHERE 
                                  balance_groups.guid= link_balance_groups_meters.guid_balance_groups and
                                  link_balance_groups_meters.guid_meters=meters.guid and
                                  taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                  taken_params.id = daily_values.id_taken_params AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  abonents.guid = link_abonents_taken_params.guid_abonents AND
                                  objects.guid = abonents.guid_objects AND
                                  names_params.guid = params.guid_names_params AND
                                  resources.guid = names_params.guid_resources AND                                  
                                  balance_groups.name = '%s' AND 
                                  daily_values.date = '%s' AND 
                                  resources.name = '%s'
                                  ) z1                       
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res, z1.ktt, z1.ktn, z1.group_name
                      order by z1.name) z2
on electric_groups.name_abonents=z2.name_abonent
where z2.group_name= '%s' ) z4, 


(Select z2.group_name,  z2.date as date_start, electric_groups.name_group, electric_groups.name_abonents, electric_groups.number_manual, z2.name_res, z2.t0 as t0_start, z2.t1 as t1_start, z2.t2 as t2_start, z2.t3 as t3_start, z2.t4 as t4_start, z2.t0r as t0r_start
from electric_groups
Left join
(SELECT z1.group_name,z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t1,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t2,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t3,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t4,
sum(Case when z1.params_name = '%s' then z1.value else null end) as t0R
                        FROM
                        (
SELECT 
                                  daily_values.date,    
                                  daily_values.value,                            
                                  abonents.name, 
                                  daily_values.id_taken_params, 
                                  objects.name as name_objects,
                                  names_params.name as params_name,
                                  meters.factory_number_manual as num_manual, 
                                  resources.name as name_res,
                                  balance_groups.name as group_name
                                FROM 
                                  public.balance_groups,
                                  public.link_balance_groups_meters,
                                  public.daily_values, 
                                  public.link_abonents_taken_params, 
                                  public.taken_params, 
                                  public.abonents, 
                                  public.objects, 
                                  public.names_params, 
                                  public.params, 
                                  public.meters, 
                                  public.resources
                                WHERE 
                                  balance_groups.guid= link_balance_groups_meters.guid_balance_groups and
                                  link_balance_groups_meters.guid_meters=meters.guid and
                                  taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                  taken_params.id = daily_values.id_taken_params AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  abonents.guid = link_abonents_taken_params.guid_abonents AND
                                  objects.guid = abonents.guid_objects AND
                                  names_params.guid = params.guid_names_params AND
                                  resources.guid = names_params.guid_resources AND                                  
                                  balance_groups.name = '%s' AND 
                                  daily_values.date = '%s' AND 
                                  resources.name = '%s'
                                  ) z1                       
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res, z1.group_name
                      order by z1.name) z2
on electric_groups.name_abonents=z2.name_abonent
where z2.group_name = '%s') z3
where z3.name_abonents=z4.name_abonents

order by z3.name_abonents ASC
    """%(params[0],params[1],params[2],params[3], params[4], params[5], obj_title, date_end, res, obj_title, 
                            params[0],params[1],params[2],params[3], params[4], params[5],obj_title,  date_start, res,obj_title)
    #print sQuery
    return sQuery

def get_data_table_electric_parametr_by_period_for_group_v2(obj_title, electric_data_start, electric_data_end, params, res):
    cursor = connection.cursor()
    cursor.execute(makeSqlQuery_electric_by_period_for_group(obj_title, electric_data_start, electric_data_end,params, res))
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table


def get_data_table_electric_parametr_by_date_monthly(obj_title, obj_parent_title, electric_data, my_parametr ):
    cursor = connection.cursor()
    cursor.execute("""SELECT 
                        monthly_values.date, objects.name, abonents.name, meters.factory_number_manual, monthly_values.value 
                        FROM
                         public.monthly_values, public.link_abonents_taken_params, public.taken_params, public.abonents, public.objects, public.names_params, public.params, public.meters 
                        WHERE
                         taken_params.guid = link_abonents_taken_params.guid_taken_params AND taken_params.id = monthly_values.id_taken_params AND taken_params.guid_params = params.guid AND taken_params.guid_meters = meters.guid AND abonents.guid = link_abonents_taken_params.guid_abonents AND objects.guid = abonents.guid_objects AND names_params.guid = params.guid_names_params AND
                        abonents.name = %s AND 
                        objects.name = %s AND 
                        names_params.name = %s AND 
                        monthly_values.date = %s 
                        ORDER BY
                        objects.name ASC
                        ;""",[obj_title, obj_parent_title, my_parametr, electric_data])
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table
    


def get_data_table_by_date_daily_2_zones(obj_title, obj_parent_title, electric_data):
    data_table = []
    
    my_parametr = "T0 A+"    
    data_table_t0_aplus = get_data_table_electric_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr)
    
    my_parametr = "T1 A+"                
    data_table_t1_aplus = get_data_table_electric_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr)

    my_parametr = "T2 A+"                
    data_table_t2_aplus = get_data_table_electric_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr)
              
    for x in range(len(data_table_t0_aplus)):
        data_table_temp = []
        try:
            data_table_temp.append(data_table_t0_aplus[x][0]) # дата
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][2]) # имя абонента
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][3]) # заводской номер
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t1_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t2_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
            
        data_table.append(data_table_temp)
    return data_table
    
    
def get_data_table_by_date_daily_3_zones(obj_title, obj_parent_title, electric_data):
    data_table = []
    
    my_parametr = "T0 A+"    
    data_table_t0_aplus = get_data_table_electric_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr)
    
    my_parametr = "T1 A+"                
    data_table_t1_aplus = get_data_table_electric_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr)

    my_parametr = "T2 A+"                
    data_table_t2_aplus = get_data_table_electric_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr)
    
    my_parametr = "T3 A+"                
    data_table_t3_aplus = get_data_table_electric_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr)
              
    for x in range(len(data_table_t0_aplus)):
        data_table_temp = []
        try:
            data_table_temp.append(data_table_t0_aplus[x][0]) # дата
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][2]) # имя абонента
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][3]) # заводской номер
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t1_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t2_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")            
        try:
            data_table_temp.append(data_table_t3_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
            
        data_table.append(data_table_temp)
    return data_table
    
def get_data_table_by_date_monthly_2_zones(obj_title, obj_parent_title, electric_data):
    data_table = []
    
    my_parametr = "T0 A+"    
    data_table_t0_aplus = get_data_table_electric_parametr_by_date_monthly(obj_title, obj_parent_title, electric_data, my_parametr)
    
    my_parametr = "T1 A+"                
    data_table_t1_aplus = get_data_table_electric_parametr_by_date_monthly(obj_title, obj_parent_title, electric_data, my_parametr)

    my_parametr = "T2 A+"                
    data_table_t2_aplus = get_data_table_electric_parametr_by_date_monthly(obj_title, obj_parent_title, electric_data, my_parametr)
              
    for x in range(len(data_table_t0_aplus)):
        data_table_temp = []
        try:
            data_table_temp.append(data_table_t0_aplus[x][0]) # дата
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][2]) # имя абонента
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][3]) # заводской номер
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t1_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t2_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
            
        data_table.append(data_table_temp)
    return data_table
    
def get_data_table_by_date_monthly_3_zones(obj_title, obj_parent_title, electric_data):
    data_table = []
    
    my_parametr = "T0 A+"    
    data_table_t0_aplus = get_data_table_electric_parametr_by_date_monthly(obj_title, obj_parent_title, electric_data, my_parametr)
    
    my_parametr = "T1 A+"                
    data_table_t1_aplus = get_data_table_electric_parametr_by_date_monthly(obj_title, obj_parent_title, electric_data, my_parametr)

    my_parametr = "T2 A+"                
    data_table_t2_aplus = get_data_table_electric_parametr_by_date_monthly(obj_title, obj_parent_title, electric_data, my_parametr)
    
    my_parametr = "T3 A+"                
    data_table_t3_aplus = get_data_table_electric_parametr_by_date_monthly(obj_title, obj_parent_title, electric_data, my_parametr)
              
    for x in range(len(data_table_t0_aplus)):
        data_table_temp = []
        try:
            data_table_temp.append(data_table_t0_aplus[x][0]) # дата
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][2]) # имя абонента
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][3]) # заводской номер
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t0_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t1_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t2_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_t3_aplus[x][4]) # значение
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
            
        data_table.append(data_table_temp)
    return data_table

def ChangeNull(data_table, electric_data):
    #обойти в цикле все строки и добавить "Н/Д" в ячейки, где null
    for i in range(len(data_table)):
        data_table[i]=list(data_table[i])
        for j in range(1,len(data_table[i])):
            if (data_table[i][j] is None):
                data_table[i][j]=u'Н/Д'
        if (electric_data is not None):
            data_table[i][0]=electric_data
        data_table[i]=tuple(data_table[i])
    return data_table

def get_data_table_by_date_for_group_3_zones_v2(obj_title, electric_data, dm):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+']
    data_table=get_data_table_electric_parametr_by_date_for_group_v2(obj_title, electric_data, params, dm)
    if len(data_table)>0:
        data_table=ChangeNull(data_table, electric_data)
    return data_table

def get_data_table_by_date_for_object_3_zones_v2(obj_title, electric_data, dm):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+']
    res=u'Электричество'
    data_table=get_data_table_electric_parametr_by_date_for_object_v2(obj_title, electric_data, params, dm,res)
    if len(data_table)>0: data_table=ChangeNull(data_table, electric_data)
    return data_table

def get_data_table_by_date_monthly_3_zones_v2(obj_title, obj_parent_title, electric_data, dm):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+']
    data_table=get_data_table_electric_parametr_by_date_monthly_v2(obj_title, obj_parent_title, electric_data, params, dm)
    if len(data_table)>0: data_table=ChangeNull(data_table, electric_data)
    return data_table
    
def get_data_table_electric_period(isAbon,obj_title,obj_parent_title, electric_data_start, electric_data_end, res, dm):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+',u'T4 A+', u'T0 R+']
    data_table=get_data_table_electric_parametr_by_period_v2(isAbon,obj_title, obj_parent_title, electric_data_start, electric_data_end, params, res, dm)
    if len(data_table)>0: data_table=ChangeNull(data_table, None)
    return data_table

def get_data_table_electric_period_for_group(obj_title,obj_parent_title, electric_data_start, electric_data_end, res):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+',u'T4 A+', u'T0 R+']
    data_table=get_data_table_electric_parametr_by_period_for_group_v2(obj_title, electric_data_start, electric_data_end, params, res)
    if len(data_table)>0: data_table=ChangeNull(data_table, None)
    return data_table

def get_daily_value_by_meter_name(meters_name, electric_data_end, parametr ):
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                                daily_values.value
                                FROM 
                                public.daily_values, 
                                public.link_abonents_taken_params, 
                                public.taken_params, 
                                public.abonents, 
                                public.objects, 
                                public.names_params, 
                                public.params, 
                                public.meters, 
                                public.resources
                                WHERE 
                                taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                taken_params.id = daily_values.id_taken_params AND
                                taken_params.guid_params = params.guid AND
                                taken_params.guid_meters = meters.guid AND
                                abonents.guid = link_abonents_taken_params.guid_abonents AND
                                objects.guid = abonents.guid_objects AND
                                names_params.guid = params.guid_names_params AND
                                resources.guid = names_params.guid_resources AND
                                abonents.name = %s AND 
                                daily_values.date = %s AND
                                names_params.name = %s AND
                                resources.name = 'Электричество'
                                ORDER BY
                                objects.name ASC;""",[meters_name, electric_data_end, parametr])
    simpleq = simpleq.fetchall()
    try:
        result = simpleq[0][0]
    except IndexError:
        result = u'Нет данных'
    return result
    
    
def get_30_min_by_meter_name(meters_name, electric_data_end, electric_data_time, parametr):
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                                  various_values.value 

                                FROM 
                                  public.various_values, 
                                  public.meters, 
                                  public.params, 
                                  public.taken_params, 
                                  public.names_params
                                WHERE 
                                  params.guid_names_params = names_params.guid AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  taken_params.id = various_values.id_taken_params AND
                                  meters.name = %s AND
                                  various_values.date = %s AND 
                                  various_values.time = %s AND 
                                  names_params.name = %s
                                 LIMIT 1;""",[meters_name, electric_data_end, electric_data_time, parametr])
    simpleq = simpleq.fetchall()
    try:
        result = simpleq[0][0]
    except IndexError:
        result = u'Нет данных'
    return result
    
    
def get_k_t_n(meter_name):
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          link_abonents_taken_params.coefficient
                        FROM 
                          public.link_abonents_taken_params, 
                          public.taken_params, 
                          public.meters
                        WHERE 
                          link_abonents_taken_params.guid_taken_params = taken_params.guid AND
                          meters.guid = taken_params.guid_meters AND
                          meters.name = %s
                          LIMIT 1;""", [meter_name])
    simpleq = simpleq.fetchall()
    return simpleq[0][0]
    
    
def get_k_t_t(meter_name):
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          link_abonents_taken_params.coefficient_2
                        FROM 
                          public.link_abonents_taken_params, 
                          public.taken_params, 
                          public.meters
                        WHERE 
                          link_abonents_taken_params.guid_taken_params = taken_params.guid AND
                          meters.guid = taken_params.guid_meters AND
                          meters.name = %s
                          LIMIT 1;""", [meter_name])
    simpleq = simpleq.fetchall()
    return simpleq[0][0]
    
def list_of_abonents_heat(parent_guid, object_name): # Отличие в сортировке
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                       abonents.name
                      FROM 
                       public.objects,
                       public.abonents
                      WHERE 
                       objects.guid = abonents.guid_objects AND
                       objects.guid_parent = %s AND
                       objects.name = %s""",[parent_guid, object_name])
    simpleq = simpleq.fetchall()
    return simpleq
    

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def get_serial_number_by_meter_name(meters_name):
    simpleq = connection.cursor()
    simpleq.execute(""" SELECT 
                         meters.factory_number_manual
                       FROM 
                         public.meters
                       WHERE 
                         meters.name = %s LIMIT 1; """,[meters_name])
    simpleq = simpleq.fetchall()
    if simpleq:
        return simpleq[0][0]
    else:
        return u'Нет данных' #Во view из AskueReports не было if-else, просто return simpleq[0][0] 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
def delta_sum_a_plus(electric_data_end): # Возвращаем потребление по группе за число по группе Литейный цех
    cursor_abonents_list = connection.cursor()
    cursor_abonents_list.execute("""
                                SELECT 
                                  meters.name,
                                  link_balance_groups_meters.type
                                FROM 
                                  public.meters, 
                                  public.link_balance_groups_meters, 
                                  public.balance_groups
                                WHERE 
                                  link_balance_groups_meters.guid_balance_groups = balance_groups.guid AND
                                  link_balance_groups_meters.guid_meters = meters.guid AND
                                  balance_groups.name = 'Литейный цех'
                                ORDER BY
                                  meters.name ASC;""")
    abonents_list = cursor_abonents_list.fetchall()
    obj_title=u'Завод'
    data_table=[]

    for x in range(len(abonents_list)):
        cursor_t0_aplus_daily_temp = connection.cursor()
        cursor_t0_aplus_daily_temp.execute("""
                    SELECT 
                      daily_values.date, 
                      daily_values.value, 
                      abonents.name, 
                      daily_values.id_taken_params, 
                      objects.name, 
                      names_params.name, 
                      meters.factory_number_manual, 
                      resources.name
                    FROM 
                      public.daily_values, 
                      public.link_abonents_taken_params, 
                      public.taken_params, 
                      public.abonents, 
                      public.objects, 
                      public.names_params, 
                      public.params, 
                      public.meters, 
                      public.resources
                    WHERE 
                      taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                      taken_params.id = daily_values.id_taken_params AND
                      taken_params.guid_params = params.guid AND
                      taken_params.guid_meters = meters.guid AND
                      abonents.guid = link_abonents_taken_params.guid_abonents AND
                      objects.guid = abonents.guid_objects AND
                      names_params.guid = params.guid_names_params AND
                      resources.guid = names_params.guid_resources AND
                      abonents.name = %s AND 
                      objects.name = %s AND 
                      names_params.name = 'T0 A+' AND 
                      daily_values.date = %s AND 
                      resources.name = 'Электричество'
                      ORDER BY
                      objects.name ASC;""",[abonents_list[x][0], obj_title, electric_data_end])
        data_table_t0_aplus_daily_temp = cursor_t0_aplus_daily_temp.fetchall()
        
        data_table_temp = []
        try:
            if abonents_list[x][1]: # Если абонент входит в группу со знаком плюс, то показания как есть
                data_table_temp.append(data_table_t0_aplus_daily_temp[0][1]*get_k_t_n(abonents_list[x][0])*get_k_t_t(abonents_list[x][0]))
            else:
                data_table_temp.append(-data_table_t0_aplus_daily_temp[0][1]*get_k_t_n(abonents_list[x][0])*get_k_t_t(abonents_list[x][0]))
        except IndexError:
            data_table_temp.append(u"Н/Д")

        data_table.append(data_table_temp)
    sum_a_plus = 0

    for x in range(len(data_table)):
        try:
            sum_a_plus = sum_a_plus + data_table[x][0]
        except:
            next
      
    if sum_a_plus:
        return sum_a_plus
    else:
        return u'Н/Д'
        
def delta_sum_r_plus(electric_data_end): # Возвращаем потребление по группе за число
    cursor_abonents_list = connection.cursor()
    cursor_abonents_list.execute("""
                        SELECT 
                          meters.name,
                          link_balance_groups_meters.type
                        FROM 
                          public.meters, 
                          public.link_balance_groups_meters, 
                          public.balance_groups
                        WHERE 
                          link_balance_groups_meters.guid_balance_groups = balance_groups.guid AND
                          link_balance_groups_meters.guid_meters = meters.guid AND
                          balance_groups.name = 'Литейный цех'
                                ORDER BY
                                  meters.name ASC;""")
    abonents_list = cursor_abonents_list.fetchall()
    obj_title=u'Завод'
    data_table=[]

    for x in range(len(abonents_list)):
        cursor_t0_rplus_daily_temp = connection.cursor()
        cursor_t0_rplus_daily_temp.execute("""
                    SELECT 
                      daily_values.date, 
                      daily_values.value, 
                      abonents.name, 
                      daily_values.id_taken_params, 
                      objects.name, 
                      names_params.name, 
                      meters.factory_number_manual, 
                      resources.name
                    FROM 
                      public.daily_values, 
                      public.link_abonents_taken_params, 
                      public.taken_params, 
                      public.abonents, 
                      public.objects, 
                      public.names_params, 
                      public.params, 
                      public.meters, 
                      public.resources
                    WHERE 
                      taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                      taken_params.id = daily_values.id_taken_params AND
                      taken_params.guid_params = params.guid AND
                      taken_params.guid_meters = meters.guid AND
                      abonents.guid = link_abonents_taken_params.guid_abonents AND
                      objects.guid = abonents.guid_objects AND
                      names_params.guid = params.guid_names_params AND
                      resources.guid = names_params.guid_resources AND
                      abonents.name = %s AND 
                      objects.name = %s AND 
                      names_params.name = 'T0 R+' AND 
                      daily_values.date = %s AND 
                      resources.name = 'Электричество'
                      ORDER BY
                      objects.name ASC;""",[abonents_list[x][0], obj_title, electric_data_end])
        data_table_t0_rplus_daily_temp = cursor_t0_rplus_daily_temp.fetchall()
        
        data_table_temp = []
        try:
            if abonents_list[x][1]: # Если абонент входит в группу со знаком плюс, то показания как есть
                data_table_temp.append(data_table_t0_rplus_daily_temp[0][1]*get_k_t_n(abonents_list[x][0])*get_k_t_t(abonents_list[x][0]))
            else:
                data_table_temp.append(-data_table_t0_rplus_daily_temp[0][1]*get_k_t_n(abonents_list[x][0])*get_k_t_t(abonents_list[x][0]))

        except IndexError:
            data_table_temp.append(u"Н/Д")

        data_table.append(data_table_temp)
    sum_r_plus = 0

    for x in range(len(data_table)):
        try:
            sum_r_plus = sum_r_plus + data_table[x][0]
        except:
            next
      
    if sum_r_plus:
        return sum_r_plus
    else:
        return u'Н/Д'
        
def product_sum(date):
    simpleq = connection.cursor()
    simpleq.execute(""" SELECT 
          sum(product_info_kilns.product_weight)
        FROM 
          public.product_info_kilns
        WHERE 
          product_info_kilns.dt = %s;""",[date])
    simpleq = simpleq.fetchall()
    return simpleq[0][0]
    
def get_daily_water_channel(meters_name, electric_data_end):
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          abonents.name, 
                          meters.name, 
                          daily_values.value, 
                          daily_values.date,
                          abonents.account_2
                        FROM 
                          public.daily_values, 
                          public.taken_params, 
                          public.meters, 
                          public.params, 
                          public.abonents, 
                          public.link_abonents_taken_params
                        WHERE 
                          daily_values.id_taken_params = taken_params.id AND
                          taken_params.guid_meters = meters.guid AND
                          params.guid = taken_params.guid_params AND
                          link_abonents_taken_params.guid_abonents = abonents.guid AND
                          link_abonents_taken_params.guid_taken_params = taken_params.guid AND
                          abonents.name = %s AND 
                          daily_values.date = %s;""",[meters_name, electric_data_end])
    simpleq = simpleq.fetchall()
    
    return simpleq
    
def makeSqlQuery_heat_sayany_by_date_for_abon(obj_title, obj_parent_title , electric_data_end, my_params):
    sQuery="""
    SELECT 

  daily_values.date, 
   
  abonents.name,   
  meters.factory_number_manual, 
sum(Case when names_params.name = '%s' then daily_values.value  end) as q1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as m1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s' AND 
  abonents.name = '%s' AND 
  daily_values.date = '%s'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name
    """%(my_params[1],my_params[2],my_params[3],my_params[4],obj_parent_title,my_params[0],obj_title,electric_data_end)
    return sQuery
    
def makeSqlQuery_heat_sayany_by_date_for_obj(obj_title, obj_parent_title , electric_data_end, my_params):
    sQuery="""
    select z1.date, heat_abons.ab_name, heat_abons.factory_number_manual, z1.q1, z1.m1,z1.t1, z1.t2
from heat_abons
left join
(
SELECT 
  daily_values.date,    
  abonents.name as ab_name,   
  meters.factory_number_manual, 
sum(Case when names_params.name = '%s' then daily_values.value  end) as q1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as m1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s' AND 
  daily_values.date = '%s'  
  group by daily_values.date,
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name
  order by abonents.name) as z1
on heat_abons.ab_name=z1.ab_name
where heat_abons.obj_name='%s'
order by heat_abons.ab_name
  

    """%(my_params[1],my_params[2],my_params[3],my_params[4],obj_title,my_params[0],electric_data_end,obj_title)
    return sQuery

def makeSqlQuery_heat_sayany_last_read_for_abon(obj_title, obj_parent_title, my_params):
    #print my_params[1],my_params[2],my_params[3],my_params[4],obj_parent_title,my_params[0],obj_title
    #print 'Query-last reded date'
    sQuery="""
    SELECT 
  daily_values.date, 
  abonents.name,   
  meters.factory_number_manual, 
sum(Case when names_params.name = '%s' then daily_values.value  end) as q1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as m1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s' AND 
  abonents.name = '%s' 
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name
 order by daily_values.date DESC
    """%(my_params[1],my_params[2],my_params[3],my_params[4],obj_parent_title,my_params[0],obj_title)
    #print 'Query-ok'
    return sQuery
    
    
def get_data_table_by_date_heat_sayany_v2(obj_title, obj_parent_title, electric_data_end, isAbon):
    my_params=[u'Sayany',u'Q Система1' ,u'M Система1',u'T Канал1',u'T Канал2' ]
    cursor = connection.cursor()
    data_table=[]
    if (isAbon) and (electric_data_end is not None):
        #print 'Abonent po date'
        cursor.execute(makeSqlQuery_heat_sayany_by_date_for_abon(obj_title, obj_parent_title , electric_data_end, my_params))
    elif isAbon and (electric_data_end is None):
        #print 'Abonent last read'
        cursor.execute(makeSqlQuery_heat_sayany_last_read_for_abon(obj_title, obj_parent_title , my_params))
    else:
        #print 'Obj po date'
        cursor.execute(makeSqlQuery_heat_sayany_by_date_for_obj(obj_title, obj_parent_title , electric_data_end, my_params))
    data_table = cursor.fetchall()
        
    
    return data_table
    
def makeSqlQuery_heat_sayany_period_for_abon(obj_title, obj_parent_title , electric_data_start, electric_data_end, my_params):
    sQuery="""
    Select z1.ab_name,z1.zav_num, z1.Q1, z2.Q1 as q2, z2.Q1-z1.Q1 as deltaQ, 
z1.m1, z2.m1 as m2, z2.m1-z1.m1 as deltam,

z1.t1, z2.t1 as t1_2, z1.t1-z2.t1 as deltat1,
z1.t2, z2.t2 as t2_2, z1.t2-z2.t2 as deltat2
From
(SELECT 
  daily_values.date as date_start, 
  objects.name as obj_name, 
  abonents.name as ab_name,   
  meters.factory_number_manual as zav_num, 
sum(Case when names_params.name = '%s' then daily_values.value  end) as q1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as m1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s' AND 
  abonents.name = '%s' AND 
  daily_values.date = '%s'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name) z1,
  (
  Select
  daily_values.date as date_end, 
  objects.name as obj_name, 
  abonents.name as ab_name,   
  meters.factory_number_manual as zav_num, 
sum(Case when names_params.name = '%s' then daily_values.value  end) as q1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as m1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s' AND 
  abonents.name = '%s' AND 
  daily_values.date = '%s'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name) z2"""%(my_params[1],my_params[2],my_params[3],my_params[4],obj_parent_title,my_params[0],obj_title,electric_data_start,my_params[1],my_params[2],my_params[3],my_params[4],obj_parent_title,my_params[0],obj_title,electric_data_end)
  
    return sQuery
    
def makeSqlQuery_heat_sayany_period_for_obj(obj_title, obj_parent_title , electric_data_start, electric_data_end, my_params):
    sQuery="""
Select heat_abons.ab_name,heat_abons.factory_number_manual, z3.q1, z3.q2, z3.deltaq, z3.m1, z3.m2, z3.deltam 
from heat_abons
left join 
(Select z1.ab_name,z1.zav_num,z1.date_start, z2.date_end, z1.Q1, z2.Q1 as q2, z2.Q1-z1.Q1 as deltaQ, 
z1.m1, z2.m1 as m2, z2.m1-z1.m1 as deltam,

z1.t1, z2.t1 as t1_2, z1.t1-z2.t1 as deltat1,
z1.t2, z2.t2 as t2_2, z1.t2-z2.t2 as deltat2
From
(SELECT 
  daily_values.date as date_start, 
  objects.name as obj_name, 
  abonents.name as ab_name,   
  meters.factory_number_manual as zav_num, 
sum(Case when names_params.name = '%s' then daily_values.value  end) as q1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as m1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s' AND 
  daily_values.date = '%s'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name) z1,
  (
  Select
  daily_values.date as date_end, 
  objects.name as obj_name, 
  abonents.name as ab_name,   
  meters.factory_number_manual as zav_num, 
sum(Case when names_params.name = '%s' then daily_values.value  end) as q1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as m1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t1,
sum(Case when names_params.name = '%s' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = '%s' AND 
  types_meters.name = '%s' AND 
  daily_values.date = '%s'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name) z2
  where z1.ab_name=z2.ab_name) z3
  on heat_abons.ab_name=z3.ab_name
  where heat_abons.obj_name='%s'
  order by heat_abons.ab_name
 
"""    %(my_params[1],my_params[2],my_params[3],my_params[4],obj_parent_title,my_params[0],electric_data_start,my_params[1],my_params[2],my_params[3],my_params[4],obj_parent_title,my_params[0],electric_data_end, obj_parent_title)
    return sQuery
    
def get_data_table_period_heat_sayany(obj_title, obj_parent_title, electric_data_start, electric_data_end, isAbon):
    my_params=[u'Sayany',u'Q Система1' ,u'M Система1',u'T Канал1',u'T Канал2' ]
    cursor = connection.cursor()
    data_table=[]
    if (isAbon) and (electric_data_end is not None):
        #print 'Abonent po date'
        cursor.execute(makeSqlQuery_heat_sayany_period_for_abon(obj_title, obj_parent_title , electric_data_start, electric_data_end, my_params))
    elif isAbon and (electric_data_end is None):
        #print 'Abonent last read'
        pass
        #cursor.execute(makeSqlQuery_heat_sayany_last_read_for_abon(obj_title, obj_parent_title , my_params))
    else:
        #print 'Obj po date'
        cursor.execute(makeSqlQuery_heat_sayany_period_for_obj( obj_parent_title,obj_title, electric_data_start, electric_data_end, my_params))
    data_table = cursor.fetchall()
            
    return data_table
    
def MakeSqlQuery_water_tekon_daily_for_abonent(obj_parent_title, obj_title, electric_data_end, chanel, my_params):
    sQuery="""
    SELECT distinct
  daily_values.date,
  water_abons.ab_name, 
  water_abons.factory_number_manual, 
  daily_values.value,
  water_abons.name AS resources_name,   
  names_params.name
FROM 
  public.water_abons, 
  public.link_abonents_taken_params, 
  public.daily_values, 
  public.taken_params, 
  public.params, 
  public.names_params
WHERE 
  link_abonents_taken_params.guid_abonents = water_abons.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid
  And
   names_params.name='%s' and
   water_abons.name='%s' and
  water_abons.ab_name='%s' and
   water_abons.obj_name='%s' and
   daily_values.date='%s' 
    """%(chanel,my_params[0], obj_title,obj_parent_title, electric_data_end)
    return sQuery
    
def MakeSqlQuery_water_tekon_daily_for_object(obj_parent_title, obj_title, electric_data_end, chanel, my_params):
    sQuery="""
    Select z1.date, water_abons.ab_name, water_abons.factory_number_manual, z1.value
from public.water_abons
left join 
(SELECT 
  daily_values.date,
  water_abons.ab_name, 
  water_abons.factory_number_manual, 
  daily_values.value,
  water_abons.name AS resources_name,   
  names_params.name
FROM 
  public.water_abons, 
  public.link_abonents_taken_params, 
  public.daily_values, 
  public.taken_params, 
  public.params, 
  public.names_params
WHERE 
  link_abonents_taken_params.guid_abonents = water_abons.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid
  And
   names_params.name='%s' and
   water_abons.name='%s' and
   water_abons.obj_name='%s' and
   daily_values.date='%s' ) as z1
   
   on water_abons.ab_name=z1.ab_name
   where water_abons.obj_name='%s' 
   order by water_abons.ab_name
    """%(chanel,my_params[0], obj_title, electric_data_end, obj_title)
    return sQuery
    
def get_data_table_tekon_daily(obj_title,obj_parent_title, electric_data_end, chanel, isAbon):
    my_params=[u'Импульс']
    cursor = connection.cursor()
    data_table=[]
    if (isAbon):
        cursor.execute(MakeSqlQuery_water_tekon_daily_for_abonent(obj_parent_title, obj_title, electric_data_end, chanel, my_params))
    else:
        cursor.execute(MakeSqlQuery_water_tekon_daily_for_object(obj_parent_title, obj_title, electric_data_end, chanel, my_params))
    data_table = cursor.fetchall()
    
    return data_table
    
def MakeSqlQuery_water_tekon_for_abonent_for_period(obj_parent_title, obj_title, electric_data_start,electric_data_end, chanel, my_params):
    sQuery="""
    Select distinct z1.ab_name, z1.factory_number_manual, z1.value, z2.value, z2.value-z1.value as delta
from
(SELECT 
  daily_values.date,
  water_abons.ab_name, 
  water_abons.factory_number_manual, 
  daily_values.value,
  water_abons.name AS resources_name,   
  names_params.name
FROM 
  public.water_abons, 
  public.link_abonents_taken_params, 
  public.daily_values, 
  public.taken_params, 
  public.params, 
  public.names_params
WHERE 
  link_abonents_taken_params.guid_abonents = water_abons.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid
  And
   names_params.name='%s' and
   water_abons.name='%s' and
   water_abons.ab_name='%s' and
   water_abons.obj_name='%s' and
   daily_values.date='%s' 
) z1,
(SELECT 
  daily_values.date,
  water_abons.ab_name, 
  water_abons.factory_number_manual, 
  daily_values.value,
  water_abons.name AS resources_name,   
  names_params.name
FROM 
  public.water_abons, 
  public.link_abonents_taken_params, 
  public.daily_values, 
  public.taken_params, 
  public.params, 
  public.names_params
WHERE 
  link_abonents_taken_params.guid_abonents = water_abons.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid
  And
   names_params.name='%s' and
   water_abons.name='%s' and
   water_abons.ab_name='%s' and
   water_abons.obj_name='%s' and
   daily_values.date='%s' 
) z2
where z1.ab_name=z2.ab_name
    """%(chanel,my_params[0], obj_title,obj_parent_title, electric_data_start, chanel,my_params[0], obj_title,obj_parent_title, electric_data_end)
    return sQuery

def MakeSqlQuery_water_tekon_for_object_for_period(obj_parent_title, obj_title, electric_data_start,electric_data_end, chanel, my_params):

    sQuery="""
    Select water_abons.ab_name, water_abons.factory_number_manual, z3.val_start, z3.val_end, z3.delta
from water_abons
left join
(Select z1.ab_name, z1.factory_number_manual, z1.value as val_start, z2.value as val_end, z2.value-z1.value as delta
from
(SELECT 
  daily_values.date,
  water_abons.ab_name, 
  water_abons.factory_number_manual, 
  daily_values.value,
  water_abons.name AS resources_name,   
  names_params.name
FROM 
  public.water_abons, 
  public.link_abonents_taken_params, 
  public.daily_values, 
  public.taken_params, 
  public.params, 
  public.names_params
WHERE 
  link_abonents_taken_params.guid_abonents = water_abons.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid
  And
   names_params.name='%s' and
   water_abons.name='%s' and   
   water_abons.obj_name='%s' and
   daily_values.date='%s' 
) z1,
(SELECT 
  daily_values.date,
  water_abons.ab_name, 
  water_abons.factory_number_manual, 
  daily_values.value,
  water_abons.name AS resources_name,   
  names_params.name
FROM 
  public.water_abons, 
  public.link_abonents_taken_params, 
  public.daily_values, 
  public.taken_params, 
  public.params, 
  public.names_params
WHERE 
  link_abonents_taken_params.guid_abonents = water_abons.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid
  And
   names_params.name='%s' and
   water_abons.name='%s' and
   water_abons.obj_name='%s' and
   daily_values.date='%s' 
) z2
where z1.ab_name=z2.ab_name) z3
on water_abons.ab_name=z3.ab_name
where water_abons.obj_name='%s' 
order by water_abons.ab_name
    """%(chanel,my_params[0], obj_title, electric_data_start,chanel,my_params[0], obj_title, electric_data_end, obj_title)
    
    return sQuery


def get_data_table_tekon_period(obj_title,obj_parent_title, electric_data_start, electric_data_end, chanel, isAbon):
    my_params=[u'Импульс']
    cursor = connection.cursor()
    data_table=[]
    if (isAbon):
        cursor.execute(MakeSqlQuery_water_tekon_for_abonent_for_period(obj_parent_title, obj_title, electric_data_start,electric_data_end, chanel, my_params))
    else:
        cursor.execute(MakeSqlQuery_water_tekon_for_object_for_period(obj_parent_title, obj_title,electric_data_start, electric_data_end, chanel, my_params))
    data_table = cursor.fetchall()
    
    return data_table
    
#Отчет по теплу на начало суток. Саяны
def get_data_table_by_date_heat_sayany(obj_title, obj_parent_title, electric_data):
    data_table = []
    
    my_parametr = "Q Система1"    
    data_table_heat_Q1       = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Sayany")
    
#    my_parametr = 'Q Система2'               
#    data_table_heat_Q2  = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Sayany")

    my_parametr = 'M Система1'               
    data_table_heat_M1      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Sayany")
#
#    my_parametr = 'M Система2'               
#    data_table_heat_M2      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Sayany")

    my_parametr = 'T Канал1'               
    data_table_heat_T1      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Sayany")
    
    my_parametr = 'T Канал2'               
    data_table_heat_T2      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Sayany")
#    
#    my_parametr = 'T Канал3'               
#    data_table_heat_T3      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Sayany")
#    
#    my_parametr = 'T Канал4'               
#    data_table_heat_T4      = get_data_table_heat_parametr_by_date_daily(obj_title, obj_parent_title, electric_data, my_parametr, u"Sayany")

              
    for x in range(len(data_table_heat_Q1)):
        data_table_temp = []
        try:
            data_table_temp.append(data_table_heat_Q1[x][0]) # дата
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_Q1[x][2]) # имя абонента
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_Q1[x][3]) # заводской номер
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_Q1[x][4]) # значение Q1
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
#        try:
#            data_table_temp.append(data_table_heat_Q2[x][4]) # значение Q2
#        except IndexError:
#            data_table_temp.append(u"Н/Д")
#        except TypeError:
#            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_M1[x][4]) # значение M1
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
#        try:
#            data_table_temp.append(data_table_heat_M2[x][4]) # значение M2
#        except IndexError:
#            data_table_temp.append(u"Н/Д")
#        except TypeError:
#            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_T1[x][4]) # значение T1
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
        try:
            data_table_temp.append(data_table_heat_T2[x][4]) # значение T2
        except IndexError:
            data_table_temp.append(u"Н/Д")
        except TypeError:
            data_table_temp.append(u"Н/Д")
#        try:
#            data_table_temp.append(data_table_heat_T3[x][4]) # значение T3
#        except IndexError:
#            data_table_temp.append(u"Н/Д")
#        except TypeError:
#            data_table_temp.append(u"Н/Д")
#        try:
#            data_table_temp.append(data_table_heat_T4[x][4]) # значение T4
#        except IndexError:
#            data_table_temp.append(u"Н/Д")
#        except TypeError:
#            data_table_temp.append(u"Н/Д")

        data_table.append(data_table_temp)
    return data_table

def return_parent_guid_by_abonent_name(object_name):
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          objects.guid
                        FROM 
                          public.objects
                        WHERE 
                          objects.name = %s;""",[object_name])
    simpleq = simpleq.fetchall()
    return simpleq[0][0]
    

def list_of_abonents(parent_guid, object_name):
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                       abonents.name
                      FROM 
                       public.objects,
                       public.abonents
                      WHERE 
                       objects.guid = abonents.guid_objects AND
                       objects.guid_parent = %s AND
                       objects.name = %s 

                       ORDER BY
                       abonents.name ASC;""",[parent_guid, object_name])
    simpleq = simpleq.fetchall()
    return simpleq

    
def list_of_objects(parent_guid): #Возвращает список объектов
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          objects.name
                        FROM 
                          public.objects
                        WHERE 
                          objects.guid_parent = %s;""",[parent_guid])
    simpleq = simpleq.fetchall()
    return simpleq
    