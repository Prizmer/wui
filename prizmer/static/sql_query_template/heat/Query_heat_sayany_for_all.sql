select z1.date, heat_abons.ab_name, heat_abons.factory_number_manual, z1.q1, z1.m1,z1.t1, z1.t2
from heat_abons
left join
(
SELECT 
objects.name,
  daily_values.date, 
   
  abonents.name as ab_name,   
  meters.factory_number_manual, 
sum(Case when names_params.name = 'Q Система1' then daily_values.value  end) as q1,
sum(Case when names_params.name = 'M Система1' then daily_values.value  end) as m1,
sum(Case when names_params.name = 'T Канал1' then daily_values.value  end) as t1,
sum(Case when names_params.name = 'T Канал2' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = 'Корпус 1А' AND 
  types_meters.name = 'Sayany' AND 
  daily_values.date = '19.03.2017'  
  group by daily_values.date,
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name
  order by abonents.name) as z1
on heat_abons.ab_name=z1.ab_name
where heat_abons.obj_name='Корпус 1А'
order by heat_abons.ab_name
  
