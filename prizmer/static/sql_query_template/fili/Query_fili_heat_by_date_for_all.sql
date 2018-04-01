Select account_2,date_install,factory_number_manual,type_energo,heat_abons_report.meter_name, z1.value,z1.date_start, substring(heat_abons_report.ab_name from 10 for char_length(heat_abons_report.ab_name)), heat_abons_report.obj_name
from heat_abons_report
Left join
(SELECT 
  daily_values.date as date_start, 
  objects.name as obj_name, 
  abonents.name as ab_name,   
  meters.factory_number_manual as zav_num, 
  meters.name as meter_name,
  daily_values.value

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

  types_meters.name = 'Sayany' AND 
  daily_values.date = '26.03.2018' and 
  names_params.name = 'Q Система1'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name,
  daily_values.value,
  meters.name
  order by objects.name, 
  abonents.name) z1
on heat_abons_report.meter_name=z1.meter_name

