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
      z2.name_group, z3.name_abonents,
      z2.number_manual, z2.t0, z2.t1, z2.t2, z2.t3
from 
(SELECT  
 abonents.name as name_abonents
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
  GROUP BY abonents.name) z3
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
      z2.number_manual, z2.t0, z2.t1, z2.t2, z2.t3
ORDER BY z3.name_abonents ASC;    """%(obj_title, params[0],params[1],params[2],params[3], obj_title, electric_data)

    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('monthly',dm)
        return sQuery
    else: return """Select 'Н/Д'"""

def get_data_table_electric_parametr_by_date_for_group_v2(obj_title, electric_data, params, dm):
    cursor = connection.cursor()
    #dm - строка, содержащая monthly or daily для sql-запроса
    cursor.execute(makeSqlQuery_electric_by_daily_or_monthly_for_group(obj_title, electric_data, params, dm))
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def makeSqlQuery_electric_by_daily_or_monthly_for_object(obj_title, electric_data, params, dm):
    sQuery="""Select  z2.monthly_date,
                      objects.name, abonents.name, 
                      z2.number_manual, z2.t0, z2.t1, z2.t2, z2.t3
                      from objects, abonents
LEFT JOIN 
(SELECT z1.monthly_date, z1.name_objects, z1.name_abonents, z1.number_manual, 
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t0,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t1,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t2,
sum(Case when z1.params_name = '%s' then z1.value_monthly  end) as t3
                        FROM
                        (SELECT monthly_values.date as monthly_date, objects.name as name_objects, abonents.name as name_abonents, meters.factory_number_manual as number_manual, monthly_values.value as value_monthly, names_params.name as params_name
                        FROM
                         public.monthly_values, public.link_abonents_taken_params, public.taken_params, public.abonents, public.objects, public.names_params, public.params, public.meters 
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND taken_params.id = monthly_values.id_taken_params AND taken_params.guid_params = params.guid AND taken_params.guid_meters = meters.guid AND abonents.guid = link_abonents_taken_params.guid_abonents AND objects.guid = abonents.guid_objects AND names_params.guid = params.guid_names_params AND
                        objects.name = '%s' AND                      
                        monthly_values.date = '%s'
                        ) z1
group by z1.name_objects, z1.monthly_date, z1.name_objects, z1.name_abonents, z1.number_manual
) z2
on abonents.name=z2.name_abonents
WHERE 
  objects.guid = abonents.guid_objects
  and objects.name='%s'
  ORDER BY abonents.name ASC;"""%(params[0],params[1],params[2],params[3], obj_title, electric_data, obj_title)

    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('monthly',dm)
        return sQuery
    else: return """Select 'Н/Д'"""
    

def get_data_table_electric_parametr_by_date_for_object_v2(obj_title, electric_data, params, dm):
    cursor = connection.cursor()
    #dm - строка, содержащая monthly or daily для sql-запроса
    cursor.execute(makeSqlQuery_electric_by_daily_or_monthly_for_object(obj_title, electric_data, params, dm))
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def makeSqlQuery_electric_by_daily_or_monthly(obj_title, obj_parent_title, electric_data, params, dm):
    sQuery="""Select z2.monthly_date,
                     abonents.name, 
                     z2.number_manual, z2.t0, z2.t1, z2.t2, z2.t3, objects.name
                     from objects, abonents
                     LEFT JOIN 
                     (SELECT z1.monthly_date, z1.name_objects, z1.name_abonents, z1.number_manual, 
                      sum(Case when z1.params_name = '%s' then z1.value_monthly else null end) as t0,
                      sum(Case when z1.params_name = '%s' then z1.value_monthly else null end) as t1,
                      sum(Case when z1.params_name = '%s' then z1.value_monthly else null end) as t2,
                      sum(Case when z1.params_name = '%s' then z1.value_monthly else null end) as t3
                        FROM
                        (SELECT monthly_values.date as monthly_date, objects.name as name_objects, abonents.name as name_abonents, meters.factory_number_manual as number_manual, monthly_values.value as value_monthly, names_params.name as params_name
                        FROM
                         public.monthly_values, public.link_abonents_taken_params, public.taken_params, public.abonents, public.objects, public.names_params, public.params, public.meters 
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND taken_params.id = monthly_values.id_taken_params AND taken_params.guid_params = params.guid AND taken_params.guid_meters = meters.guid AND abonents.guid = link_abonents_taken_params.guid_abonents AND objects.guid = abonents.guid_objects AND names_params.guid = params.guid_names_params AND
                        abonents.name = '%s' AND 
                        objects.name = '%s' AND                      
                        monthly_values.date = '%s') z1
                        group by z1.name_objects, z1.monthly_date, z1.name_objects, z1.name_abonents, z1.number_manual
                       )z2
                      on abonents.name=z2.name_abonents
                      WHERE 
                      objects.guid = abonents.guid_objects
                       and objects.name='%s'
                       and abonents.name = '%s'
                       ORDER BY abonents.name ASC;""" % (params[0],params[1],params[2],params[3],obj_title, obj_parent_title, electric_data, obj_parent_title, obj_title)
    if dm=='monthly' or dm=='daily' or dm=='current':
        sQuery=sQuery.replace('monthly',dm)
        return sQuery
    else: return """Select 'Н/Д'"""
    
def get_data_table_electric_parametr_by_date_monthly_v2(obj_title, obj_parent_title, electric_data, params, dm):
    cursor = connection.cursor()
    #dm - строка, содержащая monthly or daily для sql-запроса
    cursor.execute(makeSqlQuery_electric_by_daily_or_monthly(obj_title, obj_parent_title, electric_data, params, dm))
    data_table = cursor.fetchall()
    # 0 - дата, 1 - Имя объекта, 2 - Имя абонента, 3 - заводской номер, 4 - значение
    return data_table

def makeSqlQuery_electric_by_period(obj_title, obj_parent_title, date_start, date_end, params,res):
    sQuery="""
Select z3.ab_name, z3.factory_number_manual,
z3.t0_start, z3.t1_start, z3.t2_start, z3.t3_start, z3.t4_start, 
z4.t0_end, z4.t1_end, z4.t2_end, z4.t3_end, z4.t4_end,  
z4.t0_end-z3.t0_start as delta_t0, z4.t1_end-z3.t1_start as delta_t1, z4.t2_end-z3.t2_start as delta_t2, z4.t3_end-z3.t3_start as delta_t3, z4.t4_end-z3.t4_start as delta_t4,
z3.t0R_start, z4.t0R_end,  z4.t0R_end-z3.t0R_start as delta_t0R, z4.ktt, z4.ktn, 
z4.ktt*z4.ktn*(z4.t0_end-z3.t0_start), z4.ktt*z4.ktn*(z4.t0R_end-z3.t0R_start)
from
(Select z2.ktt, z2.ktn, z2.date as date_start, electric_abons.obj_name, electric_abons.ab_name, electric_abons.factory_number_manual, z2.name_res, z2.t0 as t0_end, z2.t1 as t1_end, z2.t2 as t2_end, z2.t3 as t3_end, z2.t4 as t4_end, z2.t0r as t0r_end
from electric_abons
Left join
(SELECT z1.ktt, z1.ktn, z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
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
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res, z1.ktt, z1.ktn
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

where z3.ab_name=z4.ab_name and z3.ab_name='%s'
ORDER BY z3.ab_name ASC;""" % (params[0],params[1],params[2],params[3], params[4], params[5],  obj_parent_title, obj_title, date_start, res, obj_parent_title, 
                            params[0],params[1],params[2],params[3], params[4], params[5],obj_parent_title, obj_title, date_end, res,obj_parent_title, obj_title)
    return sQuery

def makeSqlQuery_electric_by_period_for_all(obj_title, obj_parent_title, date_start, date_end,params, res):
    sQuery="""
    Select z3.ab_name, z3.factory_number_manual,
z3.t0_start, z3.t1_start, z3.t2_start, z3.t3_start, z3.t4_start, 
z4.t0_end, z4.t1_end, z4.t2_end, z4.t3_end, z4.t4_end,  
z4.t0_end-z3.t0_start as delta_t0, z4.t1_end-z3.t1_start as delta_t1, z4.t2_end-z3.t2_start as delta_t2, z4.t3_end-z3.t3_start as delta_t3, z4.t4_end-z3.t4_start as delta_t4,
z3.t0R_start, z4.t0R_end,  z4.t0R_end-z3.t0R_start as delta_t0R, z4.ktt, z4.ktn, 
z4.ktt*z4.ktn*(z4.t0_end-z3.t0_start), z4.ktt*z4.ktn*(z4.t0R_end-z3.t0R_start)
from
(Select z2.ktt, z2.ktn, z2.date as date_start, electric_abons.obj_name, electric_abons.ab_name, electric_abons.factory_number_manual, z2.name_res, z2.t0 as t0_end, z2.t1 as t1_end, z2.t2 as t2_end, z2.t3 as t3_end, z2.t4 as t4_end, z2.t0r as t0r_end
from electric_abons
Left join
(SELECT z1.ktt, z1.ktn, z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
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
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res, z1.ktt, z1.ktn
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
order by z3.ab_name ASC;""" % (params[0],params[1],params[2],params[3], params[4], params[5], obj_title, date_end, res, obj_title, 
                            params[0],params[1],params[2],params[3], params[4], params[5],obj_title,  date_start, res,obj_title)
    return sQuery

def get_data_table_electric_parametr_by_period_v2(isAbon,obj_title, obj_parent_title, electric_data_start, electric_data_end, params, res):
    cursor = connection.cursor()
    #isAbon - запрос для абонента или для корпуса
    if isAbon:
        cursor.execute(makeSqlQuery_electric_by_period(obj_title, obj_parent_title, electric_data_start, electric_data_end,params, res))
    else:
        cursor.execute(makeSqlQuery_electric_by_period_for_all(obj_title, obj_parent_title, electric_data_start, electric_data_end,params, res))
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
    print sQuery
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
    data_table=ChangeNull(data_table, electric_data)
    return data_table

def get_data_table_by_date_for_object_3_zones_v2(obj_title, electric_data, dm):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+']
    data_table=get_data_table_electric_parametr_by_date_for_object_v2(obj_title, electric_data, params, dm)
    data_table=ChangeNull(data_table, electric_data)
    return data_table

def get_data_table_by_date_monthly_3_zones_v2(obj_title, obj_parent_title, electric_data, dm):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+']
    data_table=get_data_table_electric_parametr_by_date_monthly_v2(obj_title, obj_parent_title, electric_data, params, dm)
    data_table=ChangeNull(data_table, electric_data)
    return data_table
    
def get_data_table_electric_period(isAbon,obj_title,obj_parent_title, electric_data_start, electric_data_end, res):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+',u'T4 A+', u'T0 R+']
    data_table=get_data_table_electric_parametr_by_period_v2(isAbon,obj_title, obj_parent_title, electric_data_start, electric_data_end, params, res)
    data_table=ChangeNull(data_table, None)
    return data_table

def get_data_table_electric_period_for_group(obj_title,obj_parent_title, electric_data_start, electric_data_end, res):
    data_table = []
    params=[u'T0 A+',u'T1 A+',u'T2 A+',u'T3 A+',u'T4 A+', u'T0 R+']
    data_table=get_data_table_electric_parametr_by_period_for_group_v2(obj_title, electric_data_start, electric_data_end, params, res)
    data_table=ChangeNull(data_table, None)
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
    