Select account_2,z2.date, water_abons_report.ab_name as meter_name,type_energo, z2.value, z2.value_old,z2.delta,date_install,z2.date_old, obj_name as ab_name
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
  public.link_abonents_taken_params,
  params,
  names_params,
  resources
WHERE 
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid 
and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  resources.name='Импульс'
  and date='09/03/2017')

SELECT 
  meters.name as meter, 
  daily_values.date as date_old, 
  daily_values.value as value_old, 
  abonents.name as ab_name, 
  abonents.guid,
  daily_values.value-z1.value as delta,
  z1.value,
  z1.date
FROM 
  public.meters, 
  public.taken_params, 
  public.daily_values, 
  public.abonents, 
  public.link_abonents_taken_params,
  params,
  names_params,
  resources, 
  z1
WHERE 
  z1.guid=abonents.guid and
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid 
and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  resources.name='Импульс' 
  and daily_values.date='31/03/2017'
)z2
on z2.ab_name=water_abons_report.ab_name
order by account_2