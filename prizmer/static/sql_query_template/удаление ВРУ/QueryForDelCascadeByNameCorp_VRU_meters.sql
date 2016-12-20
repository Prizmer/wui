Delete from daily_values
where 
daily_values.id in
(
SELECT 
  daily_values.id 
FROM 
  public.vru_no_itp, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values
WHERE 
  link_abonents_taken_params.guid_abonents = vru_no_itp.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  daily_values.id_taken_params = taken_params.id and
  obj_name='Корпус 7'
)
;

Delete from monthly_values
where 
monthly_values.id in
(
SELECT 
  monthly_values.id 
FROM 
  public.vru_no_itp, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.monthly_values
WHERE 
  link_abonents_taken_params.guid_abonents = vru_no_itp.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  monthly_values.id_taken_params = taken_params.id and
  obj_name='Корпус 7'
  )
  ;

delete from link_balance_groups_meters
where link_balance_groups_meters.guid in
(SELECT 
  link_balance_groups_meters.guid
FROM 
  public.vru_no_itp, 
  public.taken_params, 
  public.link_abonents_taken_params, 
  public.meters, 
  public.link_balance_groups_meters, 
  public.balance_groups
WHERE 
  taken_params.guid_meters = meters.guid AND
  link_abonents_taken_params.guid_abonents = vru_no_itp.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_balance_groups_meters.guid_meters = meters.guid AND
  balance_groups.guid = link_balance_groups_meters.guid_balance_groups and
  obj_name='Корпус 7'
  )
;

delete from link_meters_tcpip_settings
where link_meters_tcpip_settings.guid in
(SELECT 
  link_meters_tcpip_settings.guid
FROM 
  public.vru_no_itp, 
  public.taken_params, 
  public.link_abonents_taken_params, 
  public.meters, 
  public.link_meters_tcpip_settings
WHERE 
  taken_params.guid_meters = meters.guid AND
  link_abonents_taken_params.guid_abonents = vru_no_itp.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_meters_tcpip_settings.guid_meters = meters.guid  
  and  obj_name='Корпус 7'
  group by link_meters_tcpip_settings.guid
  )
;

delete from link_meters_comport_settings
where link_meters_comport_settings.guid in
(SELECT 
  link_meters_comport_settings.guid
FROM 
  public.vru_no_itp, 
  public.taken_params, 
  public.link_abonents_taken_params, 
  public.meters, 
  public.link_meters_comport_settings
WHERE 
  taken_params.guid_meters = meters.guid AND
  link_abonents_taken_params.guid_abonents = vru_no_itp.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_meters_comport_settings.guid_meters = meters.guid
  and  obj_name='Корпус 7'
  group by   link_meters_comport_settings.guid
  )
;


delete from  link_abonents_taken_params
where link_abonents_taken_params.guid in
(SELECT  
  link_abonents_taken_params.guid
FROM 
  public.vru_no_itp, 
  public.taken_params, 
  public.link_abonents_taken_params
WHERE 
  link_abonents_taken_params.guid_abonents = vru_no_itp.ab_guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid
  and obj_name='Корпус 7'
  group by link_abonents_taken_params.guid
)
;


  delete from abonents
  where 
  abonents.guid in
  (
 SELECT 
 abonents.guid
FROM 
  public.abonents, 
  public.objects
WHERE 
  abonents.guid_objects = objects.guid AND
  objects.name = 'Корпус 7'
  and   abonents.guid not in
  (
  SELECT 
  abonents.guid
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  objects.name = 'Корпус 7'
  group by   
  abonents.guid
  )  
    group by abonents.guid
  )
  ;





