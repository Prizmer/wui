CREATE VIEW water_pulsar_abons as
(
SELECT 
  objects.guid as obj_guid, 
  objects.name as obj_name, 
  abonents.guid as ab_guid, 
  abonents.name as ab_name, 
  meters.name as meter_name, 
  meters.factory_number_manual, 
  types_meters.name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters, 
  public.types_meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  meters.guid_types_meters = types_meters.guid and
  (types_meters.name='Пульсар ГВС' or types_meters.name='Пульсар ХВС')
  )
