select z1.date, water_abons.ab_name, water_abons.factory_number_manual, z1.hvs,z1.gvs
from water_abons
left join
(SELECT 
  current_values.date,
  objects.name as obj_name, 
  abonents.name as ab_name, 
  meters.factory_number_manual,  
   sum(Case when names_params.name = 'Канал 1' then current_values.value else null end) as hvs,
   sum(Case when names_params.name = 'Канал 2' then current_values.value else null end) as gvs
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources, 
  public.meters, 
  public.types_meters,
  current_values
WHERE 
current_values.id_taken_params=taken_params.id and
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  meters.guid_types_meters = types_meters.guid and
  resources.name='Импульс' and
  objects.name='Корпус 2'
  group by   objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  current_values.date
  order by current_values.date) z1
  on water_abons.ab_name=z1.ab_name and water_abons.obj_name=z1.obj_name
  where water_abons.obj_name='Корпус 2'
  order by water_abons.ab_name
