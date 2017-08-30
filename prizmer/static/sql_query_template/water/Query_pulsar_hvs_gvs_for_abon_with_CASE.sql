Select z2.date_end,z2.name, z2.hvs_1_num, z2.hvs_1,z2.gvs_1_num, z2.gvs_1, 
z2.hvs_2_num, z2.hvs_2,  z2.gvs_2_num,z2.gvs_2, 
z2.hvs_3_num,z2.hvs_3, z2.gvs_3_num, z2.gvs_3, 
(z2.hvs_1+z2.hvs_2+z2.hvs_3) as sum_hvs,
(z2.gvs_1+z2.gvs_2+z2.gvs_3) as sum_gvs
from 
(
Select z1.date_end, z1.name,
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
Select '30.08.2017'::text as date_end,water_pulsar_abons.ab_name as name, water_pulsar_abons.type_meter, water_pulsar_abons.attr1, water_pulsar_abons.factory_number_manual, z0.value
from water_pulsar_abons
left join
(SELECT 
  daily_values.date,  
  abonents.name, 
  substring(types_meters.name from 9 for 11),   
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
  objects.name = 'Корпус 3' AND 
  abonents.name='Квартира 003' and
  daily_values.date = '30.08.2017' and
  (types_meters.name='Пульсар ХВС' or types_meters.name='Пульсар ГВС')
) as z0
on z0.factory_number_manual=water_pulsar_abons.factory_number_manual
where water_pulsar_abons.ab_name='Квартира 003' and
water_pulsar_abons.obj_name='Корпус 3'
) as z1
group by z1.date_end,z1.name
) as z2