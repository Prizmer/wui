Select z1.ab_name, z1.type_meter, z1.attr1, z1.factory_number_manual,z1.value_start,z2.value_end, z2.value_end-z1.value_start as delta
from
(select water_pulsar_abons.ab_name, water_pulsar_abons.type_meter, water_pulsar_abons.attr1, water_pulsar_abons.factory_number_manual, z0.value as value_start
from water_pulsar_abons
left join
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
  objects.name = 'Корпус Б1' AND 

  daily_values.date = '07.09.2017' and
  (types_meters.name='Пульсар ХВС' or types_meters.name='Пульсар ГВС')
) as z0
on z0.factory_number_manual=water_pulsar_abons.factory_number_manual
where water_pulsar_abons.obj_name='Корпус Б1' 

) as z1,
(select water_pulsar_abons.ab_name, water_pulsar_abons.type_meter, water_pulsar_abons.attr1, water_pulsar_abons.factory_number_manual, z1.value as value_end
from water_pulsar_abons
left join
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
  objects.name = 'Корпус Б1' AND 

  daily_values.date = '08.09.2017' and
  (types_meters.name='Пульсар ХВС' or types_meters.name='Пульсар ГВС')
) as z1
on z1.factory_number_manual=water_pulsar_abons.factory_number_manual
where water_pulsar_abons.obj_name='Корпус Б1' 

) as z2
where z1.factory_number_manual=z2.factory_number_manual
