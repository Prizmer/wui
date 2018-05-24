Select z_start.ab_name, z_start.factory_number_manual, z_start.Q, z_end.Q, round((Z_end.Q-z_start.Q)::numeric,2), z_start.M, z_end.M, round((Z_end.M-z_start.M)::numeric,2), 
z_start.ton, z_end.ton, round((Z_end.ton-z_start.ton)::numeric,2)
from
(Select z1.date,heat_abons.obj_name, heat_abons.ab_name, heat_abons.factory_number_manual,  z1.Q,z1.M,z1.ti,z1.to,z1.ton,z1.terr, heat_abons.ab_guid
from heat_abons
left join
(SELECT 
daily_values.date,
  objects.name, 
  abonents.name,  
  meters.factory_number_manual, 
  sum(Case when names_params.name = 'Q Система1' then daily_values.value  end) as Q,
  sum(Case when names_params.name = 'M Система1' then daily_values.value  end) as M,
sum(Case when names_params.name = 'Ti' then daily_values.value  end) as ti,
sum(Case when names_params.name = 'To' then daily_values.value  end) as to,
sum(Case when names_params.name = 'Ton' then daily_values.value  end) as ton,
sum(Case when names_params.name = 'Terr' then daily_values.value  end) as terr,
abonents.guid
FROM 
  public.objects, 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params, 
  public.meters, 
  public.types_params, 
  public.resources, 
  public.names_params, 
  public.types_meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_types_params = types_params.guid AND
  params.guid_names_params = names_params.guid AND
  meters.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  daily_values.date = '23.05.2018' AND 
  types_meters.name = 'Карат 307'

  group by   
  daily_values.date,
  objects.name, 
  abonents.name,  
  meters.factory_number_manual, 
  types_meters.name,
  abonents.guid 
) z1
on z1.guid=heat_abons.ab_guid
where heat_abons.obj_name='Корпус 2' and
heat_abons.ab_name='Счётчик 15119028' and
heat_abons.type_meters = 'Карат 307'
order by heat_abons.ab_name) z_start,
(Select z1.date,heat_abons.obj_name, heat_abons.ab_name, heat_abons.factory_number_manual,  z1.Q,z1.M,z1.ti,z1.to,z1.ton,z1.terr, heat_abons.ab_guid
from heat_abons
left join
(SELECT 
daily_values.date,
  objects.name, 
  abonents.name,  
  meters.factory_number_manual, 
  sum(Case when names_params.name = 'Q Система1' then daily_values.value  end) as Q,
  sum(Case when names_params.name = 'M Система1' then daily_values.value  end) as M,
sum(Case when names_params.name = 'Ti' then daily_values.value  end) as ti,
sum(Case when names_params.name = 'To' then daily_values.value  end) as to,
sum(Case when names_params.name = 'Ton' then daily_values.value  end) as ton,
sum(Case when names_params.name = 'Terr' then daily_values.value  end) as terr,
abonents.guid
FROM 
  public.objects, 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params, 
  public.meters, 
  public.types_params, 
  public.resources, 
  public.names_params, 
  public.types_meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_types_params = types_params.guid AND
  params.guid_names_params = names_params.guid AND
  meters.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  daily_values.date = '24.05.2018' AND 
  types_meters.name = 'Карат 307'

  group by   
  daily_values.date,
  objects.name, 
  abonents.name,  
  meters.factory_number_manual, 
  types_meters.name,
  abonents.guid 
) z1
on z1.guid=heat_abons.ab_guid
where heat_abons.obj_name='Корпус 2' and
heat_abons.ab_name='Счётчик 15119028' and
heat_abons.type_meters = 'Карат 307'
order by heat_abons.ab_name) z_end
where z_start.ab_guid=z_end.ab_guid