Select heat_abons.ab_name, heat_abons.factory_number_manual, z1.energy, z1.volume

from heat_abons
left join
(SELECT 
daily_values.date,                           
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = 'Энергия' then daily_values.value else null end) as energy,
                          sum(Case when names_params.name = 'Объём' then daily_values.value else null end) as volume

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
  objects.name = 'Корпус 3' AND 
  types_meters.name = 'Эльф 1.08' and
  daily_values.date='13/09/2017'
  group by daily_values.date, objects.name, abonents.name, meters.factory_number_manual) as z1
  on heat_abons.factory_number_manual=z1.factory_number_manual
  where heat_abons.obj_name='Корпус 3'
  order by heat_abons.ab_name