Select z_end.ab_name, z_end.factory_number_manual, z_end.energy_end,z_start.energy_start,z_end.energy_end-z_start.energy_start as delta_energy, z_end.volume_end,z_start.volume_start,z_end.volume_end-z_start.volume_start as delta_volume
from
(select heat_abons.ab_name, heat_abons.factory_number_manual, z2.energy_end, z2.volume_end
from heat_abons
left join

(SELECT 
daily_values.date,                           
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = 'Энергия' then daily_values.value else null end) as energy_end,
                          sum(Case when names_params.name = 'Объем' then daily_values.value else null end) as volume_end

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
  daily_values.date='19/09/2017'
  group by daily_values.date, objects.name, abonents.name, meters.factory_number_manual) as z2
  on z2.factory_number_manual=heat_abons.factory_number_manual
  where heat_abons.obj_name='Корпус 3'
) as z_end,

(select heat_abons.ab_name, heat_abons.factory_number_manual, z1.energy_start, z1.volume_start
from heat_abons
left join
(SELECT 
daily_values.date,                           
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = 'Энергия' then daily_values.value else null end) as energy_start,
                          sum(Case when names_params.name = 'Объем' then daily_values.value else null end) as volume_start

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
  daily_values.date='18/09/2017'
  group by daily_values.date, objects.name, abonents.name, meters.factory_number_manual) as z1
  on z1.factory_number_manual=heat_abons.factory_number_manual
  where heat_abons.obj_name='Корпус 3'
) as z_start
  
  where z_start.factory_number_manual=z_end.factory_number_manual