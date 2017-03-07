Delete from daily_values
where 
daily_values.id in
(
SELECT 
  daily_values.id
FROM 
  public.objects, 
  public.taken_params, 
  public.abonents, 
  public.daily_values, 
  public.link_abonents_taken_params
WHERE 
  abonents.guid_objects = objects.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
)
;

Delete from monthly_values
where 
monthly_values.id in
(
SELECT 
  monthly_values.id
FROM 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.abonents, 
  public.objects, 
  public.monthly_values
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  abonents.guid_objects = objects.guid AND
  monthly_values.id_taken_params = taken_params.id AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
  )
  ;

delete from link_balance_groups_meters
where link_balance_groups_meters.guid in
(SELECT 
  link_balance_groups_meters.guid
FROM 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.abonents, 
  public.objects, 
  public.meters, 
  public.link_balance_groups_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  taken_params.guid_meters = meters.guid AND
  abonents.guid_objects = objects.guid AND
  link_balance_groups_meters.guid_meters = meters.guid AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
  )
;

delete from link_meters_tcpip_settings
where link_meters_tcpip_settings.guid in
(SELECT 
  link_meters_tcpip_settings.guid
FROM 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.abonents, 
  public.objects, 
  public.meters, 
  public.link_meters_tcpip_settings
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  taken_params.guid_meters = meters.guid AND
  abonents.guid_objects = objects.guid AND
  link_meters_tcpip_settings.guid_meters = meters.guid AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
  )
;

delete from link_meters_comport_settings
where link_meters_comport_settings.guid in
(SELECT 
  link_meters_comport_settings.guid
FROM 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.abonents, 
  public.objects, 
  public.meters, 
  public.link_meters_comport_settings
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  taken_params.guid_meters = meters.guid AND
  abonents.guid_objects = objects.guid AND
  link_meters_comport_settings.guid_meters = meters.guid AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
  )
;

delete from taken_params
  where  taken_params.id in
 (SELECT 
  taken_params.id
FROM 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.abonents, 
  public.objects
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  abonents.guid_objects = objects.guid AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
)
;

delete from  meters
where  meters.guid in
(SELECT 
  meters.guid
FROM 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.abonents, 
  public.objects, 
  public.meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  taken_params.guid_meters = meters.guid AND
  abonents.guid_objects = objects.guid AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
  )
;




delete from  link_abonents_taken_params
where link_abonents_taken_params.guid in
(SELECT 
  link_abonents_taken_params.guid
FROM 
  public.link_abonents_taken_params, 
  public.abonents, 
  public.objects
WHERE 
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  abonents.guid_objects = objects.guid AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
)
;

  delete from abonents
  where abonents.guid in
  (
  SELECT 
  abonents.guid
FROM 
  public.abonents, 
  public.objects
WHERE 
  abonents.guid_objects = objects.guid AND
  objects.guid = '29e8031a-9daa-4ad1-9575-10bb894f47e5'
  )
  ;

