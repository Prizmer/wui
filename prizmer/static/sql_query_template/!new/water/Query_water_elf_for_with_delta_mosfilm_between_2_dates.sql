Select z_end.ab_name, z_end.factory_number_manual, z_end.attr1,
z_end.type_res,
z_end.val_end, z_start.val_start, round((z_end.val_end-z_start.val_start)::numeric,3) as delta
from
(Select ab_name, water_abons.factory_number_manual,water_abons.attr1,z1.val_end, z1.type_res, water_abons.ab_guid
from water_abons
left join
(SELECT
  daily_values.date,
  abonents.name,  
  meters.factory_number_manual,
  abonents.guid as abon_guid,
  daily_values.value as val_end,
  taken_params.id,
  params.channel,
  abonents.guid as ab_guid,
   meters.guid,
    CASE
            WHEN params.channel = 2 THEN 'ГВ'::text
            WHEN params.channel = 1 Then 'ХВ'::text
   END as type_res,
   CASE
            WHEN params.channel = 2 THEN meters.attr2
            WHEN params.channel = 1 Then meters.attr1
   END as meter
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
  daily_values.date='01.06.2018' 
  and (channel=1 or channel=2)
ORDER BY
  abonents.name ASC) as z1
  on z1.meter=water_abons.attr1 and z1.abon_guid=water_abons.ab_guid
) as z_end,

  (Select ab_name, water_abons.factory_number_manual, z1.meter,z1.val_start, z1.type_res, water_abons.attr1,  water_abons.ab_guid
from water_abons
left join
(SELECT
  daily_values.date,
  abonents.name,  
  meters.factory_number_manual,
abonents.guid as abon_guid,
  daily_values.value as val_start,
  taken_params.id,
  params.channel,
  abonents.guid as ab_guid,
   meters.guid,
    CASE
            WHEN params.channel = 2 THEN 'ГВ'::text
            WHEN params.channel = 1 Then 'ХВ'::text
   END as type_res,
   CASE
            WHEN params.channel = 2 THEN meters.attr2
            WHEN params.channel = 1 Then meters.attr1
   END as meter
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
  daily_values.date='01.03.2018' 
  and (channel=1 or channel=2)
ORDER BY
  abonents.name ASC) as z1
  on z1.meter=water_abons.attr1 and z1.abon_guid=water_abons.ab_guid
 ) as z_start
  where z_end.attr1=z_start.attr1 and z_end.ab_guid=z_start.ab_guid and z_end.factory_number_manual=z_start.factory_number_manual
  order by z_end.ab_name