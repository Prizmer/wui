Select z_start.ab_name, z_start.type_meter, z_start.attr1, z_start.factory_number_manual,round(z_start.value::numeric,3),round(z_end.value::numeric,3), round((z_end.value-z_start.value)::numeric,3) as delta
from
(SELECT water_pulsar_abons.ab_name, water_pulsar_abons.type_meter, water_pulsar_abons.attr1, water_pulsar_abons.factory_number_manual, z1.value
from
water_pulsar_abons
Left join
(SELECT 
  objects.name, 
  abonents.name, 
  daily_values.date, 
  daily_values.value, 
  meters.name,
  meters.factory_number_manual, 
  resources.name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.resources
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  names_params.guid_resources = resources.guid AND
  daily_values.date = '24/05/2018' AND 
  (resources.name = 'ХВС' OR 
  resources.name = 'ГВС'))as z1
  on z1.factory_number_manual=water_pulsar_abons.factory_number_manual
  where water_pulsar_abons.obj_name='Корпус 2'
  order by ab_name) as z_end,
(SELECT water_pulsar_abons.ab_name, water_pulsar_abons.type_meter, water_pulsar_abons.attr1, water_pulsar_abons.factory_number_manual, z1.value
from
water_pulsar_abons
Left join
(SELECT 
  objects.name, 
  abonents.name, 
  daily_values.date, 
  daily_values.value, 
  meters.name,
  meters.factory_number_manual, 
  resources.name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.resources
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  names_params.guid_resources = resources.guid AND
  daily_values.date = '01/05/2018' AND 
  (resources.name = 'ХВС' OR 
  resources.name = 'ГВС'))as z1
  on z1.factory_number_manual=water_pulsar_abons.factory_number_manual
  where water_pulsar_abons.obj_name='Корпус 2'
  order by ab_name) as z_start
where z_end.factory_number_manual=z_start.factory_number_manual
order by z_start.ab_name, z_start.attr1, z_start.type_meter

  
