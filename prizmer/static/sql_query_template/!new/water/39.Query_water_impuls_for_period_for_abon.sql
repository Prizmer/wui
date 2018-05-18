

Select z_st.ab_name, z_st.account_2,z_st.date, z_st.meter_name,z_st.type_energo, z_st.value,z_end.value,round(z_end.value::numeric-z_st.value::numeric,3) as delta, z_st.date_install, z_end.date
from 
(Select  obj_name as ab_name, account_2,z2.date, water_abons_report.ab_name as meter_name,type_energo, z2.value,date_install
from water_abons_report
LEFT JOIN (
SELECT
  meters.name,
  daily_values.date,
  daily_values.value,
  abonents.name as ab_name,
  abonents.guid
FROM
  public.meters,
  public.taken_params,
  public.daily_values,
  public.abonents,
  public.link_abonents_taken_params,
  params,
  names_params,
  resources
WHERE
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid
and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  resources.name='Импульс'
  and date='17.05.2018'

)z2
on z2.ab_name=water_abons_report.ab_name
where water_abons_report.name='Корпус 4 Вода' and water_abons_report.obj_name='Квартира 001' 

order by account_2, obj_name) z_st,
(
Select  obj_name as ab_name, account_2,z2.date, water_abons_report.ab_name as meter_name,type_energo, z2.value,date_install
from water_abons_report
LEFT JOIN (
SELECT
  meters.name,
  daily_values.date,
  daily_values.value,
  abonents.name as ab_name,
  abonents.guid
FROM
  public.meters,
  public.taken_params,
  public.daily_values,
  public.abonents,
  public.link_abonents_taken_params,
  params,
  names_params,
  resources
WHERE
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid
and
  params.guid=taken_params.guid_params  and
  names_params.guid=params.guid_names_params and
  resources.guid=names_params.guid_resources and
  resources.name='Импульс'
  and date='18.05.2018'

)z2
on z2.ab_name=water_abons_report.ab_name
where water_abons_report.name='Корпус 4 Вода' and water_abons_report.obj_name='Квартира 001' 
order by account_2, obj_name) z_end
where z_st.meter_name=z_end.meter_name