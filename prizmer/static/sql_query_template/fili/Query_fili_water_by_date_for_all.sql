Select account_2,date_install, substring(water_abons_report.ab_name from 7 for char_length(water_abons_report.ab_name)) as factory_number,type_energo,z1.meters_name, z1.value, z1.date,substring(obj_name from 10 for char_length(obj_name)), water_abons_report.name as obj_name
from water_abons_report

LEFT JOIN 
(SELECT 
  meters.name as meters_name, 
  daily_values.date, 
  daily_values.value, 
  abonents.name as ab_name, 
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
  and date='09/03/2017') z1
  on z1.ab_name=water_abons_report.ab_name
order by account_2