CREATE OR REPLACE VIEW all_taken_params AS 
SELECT 
  objects.guid as obj_guid, 
  objects.name as obj_name, 
  abonents.guid as ab_guid, 
  abonents.name as ab_name, 
  link_abonents_taken_params.guid as link_ab_taken_guid, 
  link_abonents_taken_params.name as link_ab_taken_name, 
  taken_params.guid as taken_guid, 
  taken_params.name as taken_name, 
  meters.guid as meter_guid, 
  meters.name as meter_name, 
  meters.address as meter_adr, 
  meters.factory_number_manual
FROM 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.objects, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid

