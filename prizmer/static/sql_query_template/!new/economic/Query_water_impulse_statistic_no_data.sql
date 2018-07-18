Select water_abons_report.name as obj_name, obj_name as ab_name, water_abons_report.ab_name as meter_name,  water_abons_report.meter_name, water_abons_report.channel, z2.value 
from water_abons_report

LEFT JOIN (
SELECT 
  daily_values.date,
  obj_name as ab_name,
  abonents.name as meters,
  meters.name as meter_name,  
  names_params.name as name_params,
  daily_values.value,    
  abonents.guid,
  water_abons_report.name,
  resources.name as res
FROM 
  public.meters, 
  public.taken_params, 
  public.daily_values, 
  public.abonents, 
  public.link_abonents_taken_params,
  water_abons_report,
  params,
  names_params,
  resources
WHERE 
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  water_abons_report.ab_name=abonents.name and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  resources.name='Импульс'
  and date='09/07/2018' and
  water_abons_report.name='Лазоревый пр-д, д.1а к1 (к5) Вода'
  order by obj_name, names_params.name ) z2
  on z2.meters=water_abons_report.ab_name
  where water_abons_report.name='Лазоревый пр-д, д.1а к1 (к5) Вода'  
  and value is null
  order by obj_name, z2.name_params