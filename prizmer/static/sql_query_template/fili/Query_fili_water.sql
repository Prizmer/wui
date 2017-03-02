Select account_2,z2.date_old, ab_name as meter_name,type_energo, z2.value, z2.value_old,z2.delta,date_install,z2.date, obj_name as ab_name
from water_abons_report

LEFT JOIN (
with z1 as (SELECT 
  meters.name, 
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
  meters.name LIKE '%Пульсар%'
  and date='19/02/2017')

SELECT  
  abonents.name, 
  abonents.guid,
  daily_values.date as date_old, 
  daily_values.value as value_old,  
  z1.date,
  z1.value,
  z1.value-daily_values.value as delta
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
  meters.name LIKE '%Пульсар%'
  and daily_values.date='10/02/2017'
)z2
on z2.name=water_abons_report.ab_name