select z2.daily_date,
 z3.name_abonents,
      z2.number_manual, z3.znak*z2.t0, z3.znak*z2.t1, z3.znak*z2.t2, z3.znak*z2.t3, z3.znak
from 
(SELECT  
 abonents.name as name_abonents,
 (Case when link_balance_groups_meters.type = 'True' then 1 else -1 end)  as znak
FROM 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params,
  public.meters, 
  public.link_balance_groups_meters, 
  public.balance_groups,
  public.names_params,
  public.params
WHERE 
  taken_params.guid = link_abonents_taken_params.guid_taken_params AND 
  abonents.guid = link_abonents_taken_params.guid_abonents  AND 
  taken_params.guid_params = params.guid AND 
  names_params.guid = params.guid_names_params AND
  taken_params.guid_meters = meters.guid AND 
  meters.guid=link_balance_groups_meters.guid_meters AND
  balance_groups.guid=link_balance_groups_meters.guid_balance_groups AND
  balance_groups.name='Корпус 2 ВРУ-1' 
  GROUP BY abonents.name, link_balance_groups_meters.type) z3
Left join
(SELECT z1.guid,z1.daily_date, z1.name_group, z1.name_abonents, z1.number_manual, 
sum(Case when z1.params_name = 'T0 A+' then z1.value_daily  end) as t0,
sum(Case when z1.params_name = 'T1 A+' then z1.value_daily  end) as t1,
sum(Case when z1.params_name = 'T2 A+' then z1.value_daily  end) as t2,
sum(Case when z1.params_name = 'T3 A+' then z1.value_daily  end) as t3
FROM
                        (SELECT 
                        balance_groups.guid,
 daily_values.date as daily_date, 
 balance_groups.name as name_group, 
 abonents.name as name_abonents, 
 meters.factory_number_manual as number_manual, 
 daily_values.value as value_daily, 
 names_params.name as params_name
FROM 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params,
  public.daily_values, 
  public.meters, 
  public.link_balance_groups_meters, 
  public.balance_groups,
  public.names_params,
  public.params
WHERE 
  taken_params.guid = link_abonents_taken_params.guid_taken_params AND 
  abonents.guid = link_abonents_taken_params.guid_abonents  AND 
  taken_params.id = daily_values.id_taken_params AND 
  taken_params.guid_params = params.guid AND 
  names_params.guid = params.guid_names_params AND
  taken_params.guid_meters = meters.guid AND 
  meters.guid=link_balance_groups_meters.guid_meters AND
  balance_groups.guid=link_balance_groups_meters.guid_balance_groups AND
  balance_groups.name='Корпус 2 ВРУ-1' AND
  daily_values.date = '06.09.2016') z1
group by z1.name_group, z1.daily_date, z1.name_abonents, z1.number_manual, z1.guid
order by name_abonents ASC) z2
on z3.name_abonents=z2.name_abonents
group by z2.daily_date,
      z2.name_group, z3.name_abonents,
      z2.number_manual, z2.t0, z2.t1, z2.t2, z2.t3, z3.znak
ORDER BY z3.name_abonents ASC;