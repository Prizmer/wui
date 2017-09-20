select z_heat.ab_name, z_heat.factory_number_manual, z_heat.energy, z_heat.volume, z_water_hvs.attr1, z_water_hvs.value,z_water_gvs.attr2, z_water_gvs.value
from
(Select heat_abons.ab_name, heat_abons.factory_number_manual, z1.energy, z1.volume
from heat_abons
left join
(SELECT 
daily_values.date,                           
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = 'Энергия' then daily_values.value else null end) as energy,
                          sum(Case when names_params.name = 'Объем' then daily_values.value else null end) as volume

FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  objects.name = 'Корпус 1' AND 
  types_meters.name = 'Эльф 1.08' and
  daily_values.date='19/09/2017'
  group by daily_values.date, objects.name, abonents.name, meters.factory_number_manual) as z1
  on heat_abons.factory_number_manual=z1.factory_number_manual
  where heat_abons.obj_name='Корпус 1'
) as z_heat,
  (Select z1.date,ab_name,water_abons.factory_number_manual, z1.attr1, z1.value
from water_abons
left join
(
SELECT 
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
  params.channel = 1 and 
  daily_values.date='19.09.2017'
ORDER BY
  abonents.name ASC) as z1
  on z1.ab_guid=water_abons.ab_guid
  where water_abons.obj_name = 'Корпус 1' 
) as z_water_hvs,
(Select z1.date,ab_name,water_abons.factory_number_manual, z1.attr2, z1.value
from water_abons
left join
(
SELECT 
  daily_values.date, 
  abonents.name,   
  meters.factory_number_manual, 
  meters.attr2, 
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
  params.channel = 2 and 
  daily_values.date='19.09.2017'
ORDER BY
  abonents.name ASC) as z1
  on z1.ab_guid=water_abons.ab_guid
  where water_abons.obj_name = 'Корпус 1' 
) as z_water_gvs
where z_heat.ab_name=z_water_hvs.ab_name
and z_heat.ab_name=z_water_gvs.ab_name
order by z_heat.ab_name