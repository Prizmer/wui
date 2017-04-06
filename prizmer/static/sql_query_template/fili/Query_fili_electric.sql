Select account_2, z2.date_old, meter_name,type_energo, z2.value, z2.value_old, z2.delta,date_install,z2.date, ab_name
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
  types_meters.name LIKE '%Меркурий%230%' AND 
  daily_values.date = '31.03.2017'
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
  types_meters.name LIKE '%Меркурий%230%' AND 
  daily_values.date = '09.03.2017' and
  z1.meter_name=meters.name and
  z1.name_params=names_params.name
  order by abonents.name, 
  objects.name, meters.name) z2
  on electric_abons_report.name_meter=z2.meter_name and z2.params_name=electric_abons_report.name_params