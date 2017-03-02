Create view heat_abons_report as
SELECT 
abonents.account_2, 
meters.name as meter_name,
  'Отопление'::text as type_energo,
  '01.01.2015'::date as date_install,
  abonents.name as ab_name
FROM 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.objects, 
  public.taken_params, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  meters.name LIKE '%Sayany%'
  group by abonents.account_2,  objects.name, 
  abonents.name, 
  meters.name
