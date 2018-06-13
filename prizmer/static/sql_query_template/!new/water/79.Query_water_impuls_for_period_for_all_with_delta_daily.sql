Select z3.c_date,z3.obj_name,z3.obj_name, z3.res_name, z3.gvs,z3.hvs,
round((z3.gvs-lag(gvs)over (order by c_date))::numeric,3)  as delta_gvs,
round((z3.hvs-lag(hvs) over (order by c_date))::numeric,3) as delta_hvs
from
(Select z_date.c_date,z1.obj_name, z1.res_name, z1.gvs,z1.hvs
from
(select c_date::date
from
generate_series('01.06.2018'::timestamp without time zone, '06.06.2018'::timestamp without time zone, interval '1 day') as c_date) z_date
left join
(
SELECT
  daily_values.date, 
  water_abons_report.name as obj_name,
  resources.name as res_name,
  sum(Case when abonents.name like '%ГВС%' then daily_values.value  end) as gvs,
  sum(Case when abonents.name not like '%ГВС%' then daily_values.value  end) as hvs
FROM
  public.meters,
  public.taken_params,
  public.daily_values,
  public.abonents,
  public.link_abonents_taken_params,
  water_abons_report,
  params,
  names_params,
  resources
WHERE
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  water_abons_report.ab_name=abonents.name and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  resources.name='Импульс'
  AND
  daily_values.date between '01.06.2018' and '06.06.2018'and
  water_abons_report.name='Лазоревый пр-д, д.1а к3 (к4) Вода'
  
  group by  
  daily_values.date,  
  water_abons_report.name,
  resources.name) z1
  on z1.date=z_date.c_date
  order by z_date.c_date) z3
  
