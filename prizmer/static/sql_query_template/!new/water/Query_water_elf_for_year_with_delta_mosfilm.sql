Select z3.date,z3.ab_name,z3.factory_number_manual, z3.attr1, z3.val_end, z3.type_res, z3.channel,
round((z3.val_end-lag(val_end)over (order by z3.ab_name,z3.date))::numeric,3)  as delta_hvs
From
(Select ab_name, water_abons.factory_number_manual, z1.attr1,z1.val_end, z1.type_res, water_abons.channel, z1.date
from water_abons
left join 
(SELECT 
  daily_values.date, 
  abonents.name,   
  meters.factory_number_manual, 
  meters.attr1, 
  daily_values.value as val_end, 
  taken_params.id,   
  params.channel,
  abonents.guid as ab_guid,
   meters.guid,
  CASE
            WHEN params.channel = 2 THEN 'ГВ'::text
            WHEN params.channel = 1 Then 'ХВ'::text
   END as type_res
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
  params.channel = 1 
   and
  daily_values.date in (SELECT generate_series((Select * from 
make_date(extract(year from '15.06.2018'::timestamp)::int,extract(month from '15.06.2018'::timestamp)::int, 1)), 
(Select * from 
make_date(extract(year from '15.06.2018'::timestamp)::int,extract(month from '15.06.2018'::timestamp)::int, 1)), '1 month')::timestamp without time zone)
ORDER BY
  abonents.name ASC) as z1
  on z1.factory_number_manual=water_abons.factory_number_manual 
  order by ab_name, z1.date
  ) z3