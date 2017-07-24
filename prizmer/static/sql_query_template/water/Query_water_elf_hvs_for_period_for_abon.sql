Select z1.name,z1.factory_number_manual,z1.attr1,z1.value,z2.value, z1.value-z2.value as delta
from
(SELECT 
  daily_values.date, 
  abonents.name,   
  meters.factory_number_manual, 
  meters.attr1, 
  daily_values.value, 
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
  abonents.name = 'Квартира 411' and
  daily_values.date='24.07.2017'
ORDER BY
  abonents.name ASC) as z1,
  
(SELECT 
  daily_values.date, 
  abonents.name,   
  meters.factory_number_manual, 
  meters.attr1, 
  daily_values.value, 
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
  abonents.name = 'Квартира 411' and
  daily_values.date='24.07.2017'
ORDER BY
  abonents.name ASC) as z2
  where z1.ab_guid=z2.ab_guid
