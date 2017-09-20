Select z_end.ab_name, z_end.factory_number_manual, z_end.attr1,z_end.val_end, z_start.val_start, z_end.val_end-z_start.val_start as delta
from
(Select ab_name, water_abons.factory_number_manual, z1.attr1,z1.val_end
from water_abons
left join 
(SELECT 
  daily_values.date, 
  abonents.name,   
  meters.factory_number_manual, 
  meters.attr1, 
  daily_values.value as val_end, 
  taken_params.id,   
  params.channel,
  abonents.guid as ab_guid,
   meters.guid
FROM 
  public.meters, 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params
WHERE 
  meters.guid = taken_params.guid_meters AND
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  taken_params.id = daily_values.id_taken_params AND
  taken_params.guid_params = params.guid AND
  objects.name = 'Корпус 1' AND 
  params.channel = 1 AND 
  daily_values.date='20.09.2017'
ORDER BY
  abonents.name ASC) as z1
  on z1.factory_number_manual=water_abons.factory_number_manual 
  where water_abons.obj_name='Корпус 1') as z_end,

  (Select ab_name, water_abons.factory_number_manual, z2.attr1,z2.val_start
from water_abons
left join 
(SELECT 
  daily_values.date, 
  abonents.name,   
  meters.factory_number_manual, 
  meters.attr1, 
  daily_values.value as val_start, 
  taken_params.id,   
  params.channel,
  abonents.guid as ab_guid,
   meters.guid
FROM 
  public.meters, 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params
WHERE 
  meters.guid = taken_params.guid_meters AND
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  taken_params.id = daily_values.id_taken_params AND
  taken_params.guid_params = params.guid AND
  objects.name = 'Корпус 1' AND 
  params.channel = 1 AND 
  daily_values.date='19.09.2017'
ORDER BY
  abonents.name ASC) as z2
  on z2.factory_number_manual=water_abons.factory_number_manual
  where water_abons.obj_name='Корпус 1') as z_start
  where z_end.factory_number_manual=z_start.factory_number_manual
  order by z_end.ab_name
