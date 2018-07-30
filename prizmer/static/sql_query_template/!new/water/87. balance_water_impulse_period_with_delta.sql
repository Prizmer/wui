Select c_date,bal_name, res_name, water_minus,water_plus,delta_water_minus,delta_water_plus, delta_water_plus-delta_water_minus as nebalans, round(((( delta_water_plus-delta_water_minus ) *100)/delta_water_plus)::numeric,0) as percent, answer
from
(
Select z3.c_date,z3.bal_name, z3.res_name, z3.water_minus,z3.water_plus,
round((z3.water_minus-lag(water_minus)over (order by c_date))::numeric,3)  as delta_water_minus,
round((z3.water_plus-lag(water_plus)over (order by c_date))::numeric,3)  as delta_water_plus,
z3.answer
from
(Select z_date.c_date,z1.bal_name, z1.res_name, z1.water_plus,z1.water_minus, z1.answer
from
(select c_date::date
from
generate_series('19.07.2018'::timestamp without time zone, '24.07.2018'::timestamp without time zone, interval '1 day') as c_date) z_date
left join
(
SELECT
  daily_values.date, 
    resources.name as res_name,
    balance_groups.name as bal_name,
  sum(Case when  link_balance_groups_meters.type=False then daily_values.value end) as water_minus,
  sum(Case when  link_balance_groups_meters.type=True then daily_values.value end) as water_plus,
  count(water_abons_report.name) as answer
FROM
  public.meters,
  public.taken_params,
  public.daily_values,
  public.abonents,
  public.link_abonents_taken_params,
  water_abons_report,
  params,
  names_params,
  resources,
  link_balance_groups_meters,
  balance_groups
WHERE
  link_balance_groups_meters.guid_meters=meters.guid and
  link_balance_groups_meters.guid_balance_groups=balance_groups.guid and
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
  daily_values.date between '16.07.2018' and '24.07.2018'
  and balance_groups.name='Баланс Вода к-4-5-6'
  group by  
 
  daily_values.date,  
balance_groups.name,
  resources.name) z1
  on z1.date=z_date.c_date
  order by z_date.c_date) z3
  ) as z4
