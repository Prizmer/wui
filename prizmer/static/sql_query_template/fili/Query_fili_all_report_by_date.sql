with z3 as (Select account_2,date_install, substring(water_abons_report.ab_name from 7 for char_length(water_abons_report.ab_name)) as factory_number,type_energo,z1.meters_name, z1.value, z1.date,substring(obj_name from 10 for char_length(obj_name)) as abonent, water_abons_report.name as obj_name
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
  and date='31/03/2017') z1
  on z1.ab_name=water_abons_report.ab_name

union

Select account_2,date_install,factory_number_manual,type_energo,electric_abons_report.name_meter, z1.value,z1.date_start, substring(electric_abons_report.ab_name from 10 for char_length(electric_abons_report.ab_name)) as abonent, electric_abons_report.obj_name
from electric_abons_report
Left join
(
SELECT 
  daily_values.date as date_start, 
  objects.name as obj_name, 
  abonents.name as ab_name,   
  meters.factory_number_manual as zav_num, 
  meters.name as meter_name,
  daily_values.value,
  names_params.name as names_params
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
  types_meters.name = 'Меркурий 230' AND 
  daily_values.date = '31.03.2017'   
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name,
  daily_values.value,
  meters.name,
  names_params.name
  order by objects.name, 
  abonents.name) z1
on electric_abons_report.name_meter=z1.meter_name and z1.names_params=electric_abons_report.name_params

union

Select account_2,date_install,factory_number_manual,type_energo,heat_abons_report.meter_name, z1.value,z1.date_start, substring(heat_abons_report.ab_name from 10 for char_length(heat_abons_report.ab_name)) as abonent, heat_abons_report.obj_name
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
  daily_values.date = '31.03.2017' and 
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
on heat_abons_report.meter_name=z1.meter_name) 

Select z3.account_2,z3.date_install, z3.factory_number,z3.type_energo,z3.meters_name, z3.value, z3.date, abonent, obj_name
from z3 
order by account_2, type_energo
