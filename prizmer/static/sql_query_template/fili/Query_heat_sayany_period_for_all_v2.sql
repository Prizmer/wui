Select heat_abons.ab_name,heat_abons.factory_number_manual, z3.q1, z3.q2, z3.deltaq, z3.m1, z3.m2, z3.deltam 
from heat_abons
left join 

(Select z1.ab_name,z1.zav_num,z1.date_start, z2.date_end, z1.Q1, z2.Q1 as q2, z2.Q1-z1.Q1 as deltaQ, 
z1.m1, z2.m1 as m2, z2.m1-z1.m1 as deltam,

z1.t1, z2.t1 as t1_2, z1.t1-z2.t1 as deltat1,
z1.t2, z2.t2 as t2_2, z1.t2-z2.t2 as deltat2
From
(SELECT 
  daily_values.date as date_start, 
  objects.name as obj_name, 
  abonents.name as ab_name,   
  meters.factory_number_manual as zav_num, 
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
 
  types_meters.name = 'Sayany' AND 
  daily_values.date = '09.03.2017'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name) z1,
  (
  Select
  daily_values.date as date_end, 
  objects.name as obj_name, 
  abonents.name as ab_name,   
  meters.factory_number_manual as zav_num, 
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

  types_meters.name = 'Sayany' AND 
  daily_values.date = '31.03.2017'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name) z2
  where z1.ab_name=z2.ab_name) z3
  on heat_abons.ab_name=z3.ab_name

  order by heat_abons.ab_name

  
