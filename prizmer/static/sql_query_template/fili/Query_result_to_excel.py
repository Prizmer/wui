# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 11:07:46 2017

@author: Елена
"""

import psycopg2
from django.shortcuts import HttpResponse
import StringIO
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.styles import Style, PatternFill, Border, Side, Alignment, Font
from openpyxl.cell import get_column_letter

ali_grey   = Style(fill=PatternFill(fill_type='solid', start_color='DCDCDC'), border=Border(left=Side(border_style='thin',color='FF000000'), bottom=Side(border_style='thin',color='FF000000'), right=Side(border_style='thin',color='FF000000'), top=Side(border_style='thin',color='FF000000')), alignment = Alignment(horizontal='center', vertical='center', wrap_text=True, shrink_to_fit=True))
ali_white  = Style(border=Border(left=Side(border_style='thin',color='FF000000'), bottom=Side(border_style='thin',color='FF000000'), right=Side(border_style='thin',color='FF000000'), top=Side(border_style='thin',color='FF000000')), alignment = Alignment(horizontal='center', vertical='center', wrap_text=True, shrink_to_fit=True))
ali_yellow = Style(fill=PatternFill(fill_type='solid', start_color='EEEE00'), border=Border(left=Side(border_style='thin',color='FF000000'), bottom=Side(border_style='thin',color='FF000000'), right=Side(border_style='thin',color='FF000000'), top=Side(border_style='thin',color='FF000000')), alignment = Alignment(horizontal='center', vertical='center', wrap_text=True, shrink_to_fit=True))
ali_white_size_18  = Style(font=Font(size=18))

def makeSqlQuery_report_all_period( electric_data_start, electric_data_end):
    sQuery="""
Select account_2,%s::date as date_start, ab_name as meter_name,z2.factory_number_manual,type_energo, z2.value, z2.value_old,z2.delta,date_install,%s::date as date_end, obj_name as ab_name
from water_abons_report
LEFT JOIN (
with z1 as (SELECT 
  meters.name, 
  meters.factory_number_manual,
  daily_values.date, 
  daily_values.value, 
  abonents.name, 
  abonents.guid
FROM 
  public.meters, 
  public.taken_params, 
  public.daily_values, 
  public.abonents, 
  public.link_abonents_taken_params
WHERE 
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  meters.name LIKE '%%Пульсар%%'
  and date=%s)
SELECT  
  abonents.name, 
  abonents.guid,
  daily_values.date as date_old, 
  daily_values.value as value_old,  
  z1.date,
  z1.value,
  z1.value-daily_values.value as delta,
  z1.factory_number_manual
FROM 
  z1,
  public.meters, 
  public.taken_params, 
  public.daily_values, 
  public.abonents, 
  public.link_abonents_taken_params
WHERE 
  z1.guid=abonents.guid and
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  meters.name LIKE '%%Пульсар%%'
  and daily_values.date=%s
)z2
on z2.name=water_abons_report.ab_name
union
Select account_2,%s::date as date_start, meter_name,z2.factory_number_manual,type_energo, z2.value_old, z2.value,z2.delta,date_install,%s::date as date_end, ab_name
from heat_abons_report
LEFT JOIN
(with z1 as (SELECT 
  abonents.name, 
  objects.name, 
  daily_values.date as date_old, 
  daily_values.value as value_old, 
  meters.name as name_meters,
  meters.factory_number_manual,
  params.name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters,
  params
WHERE 
  taken_params.guid_params=params.guid and
   abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.name LIKE '%%Sayany%%' and
  daily_values.date = %s and
   params.name='Саяны Комбик Q Система1 Суточный -- adress: 0  channel: 1'
  group by 
  abonents.name, 
  objects.name, 
  daily_values.date, 
  daily_values.value, 
  meters.name,
  meters.factory_number_manual,
  params.name)
  SELECT 
  abonents.name, 
  objects.name, 
  z1.date_old,
  z1.value_old,
  daily_values.date, 
  daily_values.value, 
  meters.name as name_meters,
  params.name,
  z1.factory_number_manual,
  z1.value_old-daily_values.value as delta
FROM 
  z1,
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters,
  params
WHERE 
  taken_params.guid_params=params.guid and
   abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.name LIKE '%%Sayany%%' and
  daily_values.date = %s and
  params.name='Саяны Комбик Q Система1 Суточный -- adress: 0  channel: 1'
  and meters.name = z1.name_meters
  group by 
  z1.factory_number_manual,
  abonents.name, 
  objects.name, 
  daily_values.date, 
  daily_values.value, 
  meters.name,
  params.name,
  z1.date_old,
  z1.value_old) z2
  on z2.name_meters=heat_abons_report.meter_name
union
Select account_2, %s::date as date_start, meter_name,z2.factory_number_manual,type_energo, z2.value, z2.value_old, z2.delta,date_install,%s::date as date_end, ab_name
from electric_abons_report
LEFT JOIN
(with z1 as 
(SELECT 
  abonents.name, 
  objects.name, 
  daily_values.date, 
  daily_values.value, 
  names_params.name as name_params, 
  types_meters.name, 
  meters.factory_number_manual,
  meters.name as meter_name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  types_meters.name LIKE '%%Меркурий%%230%%' AND 
  daily_values.date = %s
)
SELECT 
  abonents.name, 
  objects.name, 
  z1.date,
  z1.value,
  daily_values.date as date_old, 
  daily_values.value as value_old, 
  names_params.name as params_name, 
  types_meters.name, 
  meters.factory_number_manual,
  meters.name as meter_name,
  z1.value-daily_values.value as delta
FROM 
z1,
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  types_meters.name LIKE '%%Меркурий%%230%%' AND 
  daily_values.date = %s and
  z1.meter_name=meters.name and
  z1.name_params=names_params.name
  order by abonents.name, 
  objects.name, meters.name) z2
  on electric_abons_report.name_meter=z2.meter_name and z2.params_name=electric_abons_report.name_params;
    """%(electric_data_start,electric_data_end,electric_data_end,electric_data_start, electric_data_start,electric_data_end,electric_data_end,electric_data_start, electric_data_start,electric_data_end, electric_data_end,electric_data_start)
    #print sQuery
    #print (electric_data_start,electric_data_end,electric_data_end,electric_data_start, electric_data_start,electric_data_end,electric_data_end,electric_data_start, electric_data_start,electric_data_end, electric_data_end,electric_data_start)
    #print len([electric_data_start,electric_data_end,electric_data_end,electric_data_start, electric_data_start,electric_data_end,electric_data_end,electric_data_start, electric_data_start,electric_data_end, electric_data_end,electric_data_start])
    return sQuery
    

connection = psycopg2.connect(host='localhost',
                             port=5432,
                             dbname='prizmer',
                             user='postgres',
                             password='1')
cursor=connection.cursor()
print 'connection Ok'
electric_data_start=u'10.02.2017'
electric_data_end=u'19.02.2017'
cursor.execute(
"""Select account_2,%s::date as date_start, ab_name as meter_name,z2.factory_number_manual,type_energo, z2.value, z2.value_old,z2.delta,date_install,%s::date as date_end, obj_name as ab_name
from water_abons_report
LEFT JOIN (
with z1 as (SELECT 
  meters.name, 
  meters.factory_number_manual,
  daily_values.date, 
  daily_values.value, 
  abonents.name, 
  abonents.guid
FROM 
  public.meters, 
  public.taken_params, 
  public.daily_values, 
  public.abonents, 
  public.link_abonents_taken_params
WHERE 
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  meters.name LIKE '%%Пульсар%%'
  and date=%s)
SELECT  
  abonents.name, 
  abonents.guid,
  daily_values.date as date_old, 
  daily_values.value as value_old,  
  z1.date,
  z1.value,
  z1.value-daily_values.value as delta,
  z1.factory_number_manual
FROM 
  z1,
  public.meters, 
  public.taken_params, 
  public.daily_values, 
  public.abonents, 
  public.link_abonents_taken_params
WHERE 
  z1.guid=abonents.guid and
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  meters.name LIKE '%%Пульсар%%'
  and daily_values.date=%s
)z2
on z2.name=water_abons_report.ab_name
union
Select account_2,%s::date as date_start, meter_name,z2.factory_number_manual,type_energo, z2.value_old, z2.value,z2.delta,date_install,%s::date as date_end, ab_name
from heat_abons_report
LEFT JOIN
(with z1 as (SELECT 
  abonents.name, 
  objects.name, 
  daily_values.date as date_old, 
  daily_values.value as value_old, 
  meters.name as name_meters,
  meters.factory_number_manual,
  params.name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters,
  params
WHERE 
  taken_params.guid_params=params.guid and
   abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.name LIKE '%%Sayany%%' and
  daily_values.date = %s and
   params.name='Саяны Комбик Q Система1 Суточный -- adress: 0  channel: 1'
  group by 
  abonents.name, 
  objects.name, 
  daily_values.date, 
  daily_values.value, 
  meters.name,
  meters.factory_number_manual,
  params.name)
  SELECT 
  abonents.name, 
  objects.name, 
  z1.date_old,
  z1.value_old,
  daily_values.date, 
  daily_values.value, 
  meters.name as name_meters,
  params.name,
  z1.factory_number_manual,
  z1.value_old-daily_values.value as delta
FROM 
  z1,
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters,
  params
WHERE 
  taken_params.guid_params=params.guid and
   abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.name LIKE '%%Sayany%%' and
  daily_values.date = %s and
  params.name='Саяны Комбик Q Система1 Суточный -- adress: 0  channel: 1'
  and meters.name = z1.name_meters
  group by 
  z1.factory_number_manual,
  abonents.name, 
  objects.name, 
  daily_values.date, 
  daily_values.value, 
  meters.name,
  params.name,
  z1.date_old,
  z1.value_old) z2
  on z2.name_meters=heat_abons_report.meter_name
union
Select account_2, %s::date as date_start, meter_name,z2.factory_number_manual,type_energo, z2.value, z2.value_old, z2.delta,date_install,%s::date as date_end, ab_name
from electric_abons_report
LEFT JOIN
(with z1 as 
(SELECT 
  abonents.name, 
  objects.name, 
  daily_values.date, 
  daily_values.value, 
  names_params.name as name_params, 
  types_meters.name, 
  meters.factory_number_manual,
  meters.name as meter_name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  types_meters.name LIKE '%%Меркурий%%230%%' AND 
  daily_values.date = %s
)
SELECT 
  abonents.name, 
  objects.name, 
  z1.date,
  z1.value,
  daily_values.date as date_old, 
  daily_values.value as value_old, 
  names_params.name as params_name, 
  types_meters.name, 
  meters.factory_number_manual,
  meters.name as meter_name,
  z1.value-daily_values.value as delta
FROM 
z1,
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  types_meters.name LIKE '%%Меркурий%%230%%' AND 
  daily_values.date = %s and
  z1.meter_name=meters.name and
  z1.name_params=names_params.name
  order by abonents.name, 
  objects.name, meters.name) z2
  on electric_abons_report.name_meter=z2.meter_name and z2.params_name=electric_abons_report.name_params;
    """,[electric_data_start,electric_data_end,electric_data_end,electric_data_start, electric_data_start,electric_data_end,electric_data_end,electric_data_start, electric_data_start,electric_data_end, electric_data_end,electric_data_start]
)
data_table = cursor.fetchall()
print data_table
#report_resources_all(data_table)
