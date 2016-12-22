Select z1.date, water_abons.ab_name, water_abons.factory_number_manual, z1.value
from public.water_abons
left join 
(SELECT 
  daily_values.date,
  abonents.name as ab_name, 
  meters.factory_number_manual ,
  daily_values.value 
  
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.names_params, 
  public.params, 
  public.resources, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  names_params.guid_resources = resources.guid AND
  params.guid_names_params = names_params.guid
And
   names_params.name='Канал 1' and
   resources.name='Импульс' and
   abonents.name='Квартира 0640' and
   objects.name='Корпус 7' and
   daily_values.date='20.12.2016'   
 ) as z1
   
   on water_abons.ab_name=z1.ab_name
   where water_abons.obj_name='Корпус 7' 
   and water_abons.names_params='Канал 1'
   order by water_abons.ab_name
