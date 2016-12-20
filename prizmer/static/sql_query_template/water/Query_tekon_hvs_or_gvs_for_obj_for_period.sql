Select water_abons.ab_name, water_abons.factory_number_manual, z3.val_start, z3.val_end, z3.delta
from water_abons
left join
(Select z1.ab_name, z1.factory_number_manual, z1.value as val_start, z2.value as val_end, z2.value-z1.value as delta
from
(SELECT 
  daily_values.date,
  water_abons.ab_name, 
  water_abons.factory_number_manual, 
  daily_values.value,
  water_abons.name AS resources_name,   
  names_params.name
FROM 
  public.water_abons, 
  public.link_abonents_taken_params, 
  public.daily_values, 
  public.taken_params, 
  public.params, 
  public.names_params
WHERE 
  link_abonents_taken_params.guid_abonents = water_abons.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid
  And
   names_params.name='Канал 1' and
   water_abons.name='Импульс' and   
   water_abons.obj_name='Корпус 7' and
   daily_values.date='19.12.2016' 
) z1,
(SELECT 
  daily_values.date,
  water_abons.ab_name, 
  water_abons.factory_number_manual, 
  daily_values.value,
  water_abons.name AS resources_name,   
  names_params.name
FROM 
  public.water_abons, 
  public.link_abonents_taken_params, 
  public.daily_values, 
  public.taken_params, 
  public.params, 
  public.names_params
WHERE 
  link_abonents_taken_params.guid_abonents = water_abons.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid
  And
   names_params.name='Канал 1' and
   water_abons.name='Импульс' and
   water_abons.obj_name='Корпус 7' and
   daily_values.date='20.12.2016' 
) z2
where z1.ab_name=z2.ab_name) z3
on water_abons.ab_name=z3.ab_name
where water_abons.obj_name='Корпус 7' 
order by water_abons.ab_name
