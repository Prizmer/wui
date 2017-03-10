Select account_2,'09.02.2017'::date as date_start, z2.factory_number_manual as meter_name,ab_name, type_energo, z2.value, z2.value_old,z2.delta,date_install,'20.02.2017'::date as date_end, obj_name as ab_name
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
  public.link_abonents_taken_params,
  params,
  names_params,
  resources
WHERE 
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  resources.name='Импульс'
  and date='19/02/2017')

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
  public.link_abonents_taken_params,
  params,
  names_params,
  resources
WHERE 
  z1.guid=abonents.guid and
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  resources.name='Импульс'
  and daily_values.date='10/02/2017'
)z2
on z2.name=water_abons_report.ab_name

union

Select account_2,'09.02.2017'::date as date_start, meter_name,z2.factory_number_manual,type_energo, z2.value_old, z2.value,z2.delta,date_install,'20.02.2017'::date as date_end, ab_name
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
  params,
  names_params,
  resources
WHERE 
  taken_params.guid_params=params.guid and
   abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  daily_values.date = '19.02.2017' and
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
  params,
  names_params,
  resources
WHERE 
  taken_params.guid_params=params.guid and
   abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  daily_values.date = '09.02.2017' and
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

Select account_2, '09.02.2017'::date as date_start, meter_name,z2.factory_number_manual,type_energo, z2.value, z2.value_old, z2.delta,date_install,'20.02.2017'::date as date_end, ab_name
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
  public.meters,
  resources
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND

  resources.guid=names_params.guid_resources and
  resources.name='Электричество' and
  daily_values.date = '20.02.2017'
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
  public.meters,
  resources
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
   resources.guid=names_params.guid_resources and
  resources.name='Электричество' and
  daily_values.date = '10.02.2017' and
  z1.meter_name=meters.name and
  z1.name_params=names_params.name
  order by abonents.name, 
  objects.name, meters.name) z2
  on electric_abons_report.name_meter=z2.meter_name and z2.params_name=electric_abons_report.name_params
  order by  account_2