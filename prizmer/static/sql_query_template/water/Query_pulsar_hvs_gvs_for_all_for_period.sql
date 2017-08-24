Select water_pulsar_abons.ab_name, z3.type_meters, z3.attr1, water_pulsar_abons.factory_number_manual, z3.val_start,z3.val_end, z3.delta
from water_pulsar_abons
Left Join
(Select z1.name, z1.type_meters, z1.attr1, z1.factory_number_manual,z1.value as val_start,z2.value as val_end, z2.value-z1.value as delta
from
(SELECT 
  daily_values.date,  
  abonents.name, 
  substring(types_meters.name from 9 for 11) as type_meters,   
  meters.attr1,
  meters.factory_number_manual,   
  daily_values.value,   
  abonents.guid
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  objects.name = 'Корпус 2' AND 
  daily_values.date = '11.08.2017' and
  (types_meters.name='Пульсар ХВС' or types_meters.name='Пульсар ГВС')
ORDER BY
  abonents.name ASC
) as z1,
(SELECT 
  daily_values.date,  
  abonents.name, 
  substring(types_meters.name from 9 for 11)as type_meters,
   
  meters.attr1,
  meters.factory_number_manual,   
  daily_values.value,   
  abonents.guid
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  objects.name = 'Корпус 2' AND 
  daily_values.date = '14.08.2017' and
  (types_meters.name='Пульсар ХВС' or types_meters.name='Пульсар ГВС')
ORDER BY
  abonents.name ASC
) as z2
where z1.factory_number_manual=z2.factory_number_manual) as z3
on water_pulsar_abons.factory_number_manual=z3.factory_number_manual
where water_pulsar_abons.obj_name='Корпус 2'
order by water_pulsar_abons.ab_name, z3.type_meters, z3.attr1