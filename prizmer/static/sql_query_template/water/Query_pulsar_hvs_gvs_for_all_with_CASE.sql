Select z4.date_val, z4.ab_name,z4.hvs_1_num, z4.hvs_1,z4.gvs_1_num, z4.gvs_1, 
z4.hvs_2_num, z4.hvs_2,  z4.gvs_2_num,z4.gvs_2, 
z4.hvs_3_num,z4.hvs_3, z4.gvs_3_num, z4.gvs_3, 
z4.sum_hvs,
z4.sum_gvs
from
(select z3.date as date_val, water_pulsar_abons.ab_name, z3.date, z3.hvs_1_num, z3.hvs_1,z3.gvs_1_num, z3.gvs_1, 
z3.hvs_2_num, z3.hvs_2,  z3.gvs_2_num,z3.gvs_2, 
z3.hvs_3_num,z3.hvs_3, z3.gvs_3_num, z3.gvs_3, 
z3.sum_hvs,
z3.sum_gvs
from water_pulsar_abons
left join
(Select z2.date,z2.name, z2.hvs_1_num, z2.hvs_1,z2.gvs_1_num, z2.gvs_1, 
z2.hvs_2_num, z2.hvs_2,  z2.gvs_2_num,z2.gvs_2, 
z2.hvs_3_num,z2.hvs_3, z2.gvs_3_num, z2.gvs_3, 
(z2.hvs_1+z2.hvs_2+z2.hvs_3) as sum_hvs,
(z2.gvs_1+z2.gvs_2+z2.gvs_3) as sum_gvs
from 
(
Select z1.date,z1.name,z1.guid, 
sum(Case when z1.attr1 = 'Стояк 1' and z1.type_meter='ХВС'  then z1.factory_number_manual::bigint  end) as hvs_1_num,
sum(Case when z1.attr1 = 'Стояк 1' and z1.type_meter='ХВС'  then z1.value else 0 end) as hvs_1,
sum(Case when z1.attr1 = 'Стояк 1' and z1.type_meter='ГВС'  then z1.factory_number_manual::bigint  end) as gvs_1_num,
sum(Case when z1.attr1 = 'Стояк 1' and z1.type_meter='ГВС'  then z1.value else 0 end) as gvs_1,
sum(Case when z1.attr1 = 'Стояк 2' and z1.type_meter='ХВС'  then z1.factory_number_manual::bigint end) as hvs_2_num,
sum(Case when z1.attr1 = 'Стояк 2' and z1.type_meter='ХВС'  then z1.value else 0  end) as hvs_2,
sum(Case when z1.attr1 = 'Стояк 2' and z1.type_meter='ГВС'  then z1.factory_number_manual::bigint end) as gvs_2_num,
sum(Case when z1.attr1 = 'Стояк 2' and z1.type_meter='ГВС'  then z1.value else 0  end) as gvs_2,
sum(Case when z1.attr1 = 'Стояк 3' and z1.type_meter='ХВС'  then z1.factory_number_manual::bigint  end) as hvs_3_num,
sum(Case when z1.attr1 = 'Стояк 3' and z1.type_meter='ХВС'  then z1.value else 0  end) as hvs_3,
sum(Case when z1.attr1 = 'Стояк 3' and z1.type_meter='ГВС'  then z1.factory_number_manual::bigint  end) as gvs_3_num,
sum(Case when z1.attr1 = 'Стояк 3' and z1.type_meter='ГВС'  then z1.value else 0  end) as gvs_3
from
(
SELECT 
  daily_values.date,  
  abonents.name, 
  substring(types_meters.name from 9 for 11) as type_meter,   
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
) as z1
group by z1.date,z1.name,z1.guid) as z2) as z3
on water_pulsar_abons.ab_name=z3.name
where water_pulsar_abons.obj_name= 'Корпус 2'
) as z4

group by z4.date_val, z4.ab_name, z4.date, z4.hvs_1_num, z4.hvs_1,z4.gvs_1_num, z4.gvs_1, 
z4.hvs_2_num, z4.hvs_2,  z4.gvs_2_num,z4.gvs_2, 
z4.hvs_3_num,z4.hvs_3, z4.gvs_3_num, z4.gvs_3, 
z4.sum_hvs,
z4.sum_gvs
order by  z4.ab_name