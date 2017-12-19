select z_start.ab_name,  z_start.gvs_1_num, z_start.gvs_1, z_start.date_start,z_end.gvs_1, z_end.date_end,round((z_end.gvs_1-z_start.gvs_1)::numeric,3) , z_end.hvs_1_num, z_start.hvs_1, z_start.date_start,   z_end.hvs_1,  z_end.date_end,round((z_end.hvs_1-z_start.hvs_1)::numeric,3)
from

(select water_pulsar_abons.ab_name,water_pulsar_abons.ab_guid, z3.gvs_1_num, z3.gvs_1, z3.date, z3.hvs_1_num, z3.hvs_1,   z3.date as date_start
from water_pulsar_abons
left join
(Select *
from
(
Select z1.date,z1.name,z1.guid, 
sum(Case when  z1.type_meter='ХВС'  then z1.factory_number_manual::bigint  end) as hvs_1_num,
sum(Case when  z1.type_meter='ХВС'  then z1.value else 0 end) as hvs_1,
sum(Case when z1.type_meter='ГВС'  then z1.factory_number_manual::bigint  end) as gvs_1_num,
sum(Case when  z1.type_meter='ГВС'  then z1.value else 0 end) as gvs_1

from
(
SELECT 
  daily_values.date,  
  abonents.name, 
  substring(types_meters.name from 9 for 11)as type_meter,
   
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

  daily_values.date = '05.11.2017' and
  (types_meters.name='Пульсар ХВС' or types_meters.name='Пульсар ГВС')
) as z1
group by z1.date,z1.name,z1.guid) as z2) as z3
on  water_pulsar_abons.ab_guid=z3.guid
where water_pulsar_abons.obj_name='Корпус Б1'
group by water_pulsar_abons.ab_name, z3.hvs_1_num, z3.hvs_1, z3.gvs_1_num, z3.gvs_1,z3.date, water_pulsar_abons.ab_guid
order by water_pulsar_abons.ab_name) as z_start,

(select water_pulsar_abons.ab_name,water_pulsar_abons.ab_guid, z3.gvs_1_num, z3.gvs_1, z3.date, z3.hvs_1_num, z3.hvs_1,   z3.date as date_end
from water_pulsar_abons
left join
(Select *
from
(
Select z1.date,z1.name,z1.guid, 
sum(Case when  z1.type_meter='ХВС'  then z1.factory_number_manual::bigint  end) as hvs_1_num,
sum(Case when  z1.type_meter='ХВС'  then z1.value else 0 end) as hvs_1,
sum(Case when z1.type_meter='ГВС'  then z1.factory_number_manual::bigint  end) as gvs_1_num,
sum(Case when  z1.type_meter='ГВС'  then z1.value else 0 end) as gvs_1

from
(
SELECT 
  daily_values.date,  
  abonents.name, 
  substring(types_meters.name from 9 for 11)as type_meter,
   
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

  daily_values.date = '29.11.2017' and
  (types_meters.name='Пульсар ХВС' or types_meters.name='Пульсар ГВС')
) as z1
group by z1.date,z1.name,z1.guid) as z2) as z3
on  water_pulsar_abons.ab_guid=z3.guid
where water_pulsar_abons.obj_name='Корпус Б1'
and water_pulsar_abons.ab_name='Квартира 001'
group by water_pulsar_abons.ab_name, z3.hvs_1_num, z3.hvs_1, z3.gvs_1_num, z3.gvs_1,z3.date, water_pulsar_abons.ab_guid
order by water_pulsar_abons.ab_name) as z_end
where z_end.ab_guid=z_start.ab_guid