Select account_2,z2.date_old, meter_name,type_energo, z2.value, z2.value_old,z2.delta,date_install,z2.date, ab_name
from heat_abons_report
LEFT JOIN
(with z1 as (SELECT 
  abonents.name, 
  objects.name, 
  daily_values.date as date_old, 
  daily_values.value as value_old, 
  meters.name as name_meters,
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
  meters.name LIKE '%Sayany%' and
  daily_values.date = '09.02.2017' and
   params.name='Саяны Комбик Q Система1 Суточный -- adress: 0  channel: 1'
  group by 
  abonents.name, 
  objects.name, 
  daily_values.date, 
  daily_values.value, 
  meters.name,
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
  daily_values.value-z1.value_old as delta
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
  meters.name LIKE '%Sayany%' and
  daily_values.date = '19.02.2017' and
  params.name='Саяны Комбик Q Система1 Суточный -- adress: 0  channel: 1'
  and meters.name = z1.name_meters
  group by 
  abonents.name, 
  objects.name, 
  daily_values.date, 
  daily_values.value, 
  meters.name,
  params.name,
  z1.date_old,
  z1.value_old) z2
  on z2.name_meters=heat_abons_report.meter_name
