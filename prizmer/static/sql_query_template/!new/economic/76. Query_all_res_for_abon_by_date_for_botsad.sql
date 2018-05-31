Select water_abons_report.ab_name as meter,
 type_energo,water_abons_report.meter_name, z1.value, z1.date, 
 water_abons_report.obj_name as water_ab_name,
  water_abons_report.name as obj_name
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
  and date='31.05.2018') z1
  on z1.ab_name=water_abons_report.ab_name
  where water_abons_report.name ='Корпус 4 Вода'
  and water_abons_report.obj_name='Квартира 001'

  union

  Select name_meter,type_energo,electric_abons_without_sum_report.factory_number_manual, z1.value,z1.date_start, electric_abons_without_sum_report.ab_name, electric_abons_without_sum_report.obj_name
from electric_abons_without_sum_report
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
  public.names_params,
  resources
WHERE
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  resources.guid=names_params.guid_resources and
  resources.name='Электричество' and
  daily_values.date = '31.05.2018'
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
on electric_abons_without_sum_report.name_meter=z1.meter_name and z1.names_params=electric_abons_without_sum_report.name_params
where electric_abons_without_sum_report.ab_name='Квартира 001' and
 electric_abons_without_sum_report.obj_name='Корпус 4'

 union

 Select type_meter::text||' '||factory_number_manual::text, name_param,factory_number_manual, z1.value,z1.date_start, heat_abons.ab_name, heat_abons.obj_name
from heat_abons
Left join
(SELECT
  daily_values.date as date_start,
  objects.name as obj_name,
  abonents.name as ab_name,
  meters.factory_number_manual as zav_num,
  meters.name as meter_name,
  daily_values.value,
  types_meters.name as type_meter,
  names_params.name as name_param
FROM
  public.abonents,
  public.objects,
  public.link_abonents_taken_params,
  public.taken_params,
  public.daily_values,
  public.meters,
  public.types_meters,
  public.params,
  public.names_params,
  resources
WHERE
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  resources.guid=names_params.guid_resources and
  resources.name='Тепло' and
  daily_values.date = '31.05.2018' 
  group by daily_values.date,
  objects.name,
  abonents.name,
  meters.factory_number_manual,
  types_meters.name,
  daily_values.value,
  meters.name, names_params.name
  order by objects.name,
  abonents.name) z1
on heat_abons.factory_number_manual=z1.zav_num
where heat_abons.ab_name='Квартира 001' and 
heat_abons.obj_name='Корпус 4'

order by meter, type_energo