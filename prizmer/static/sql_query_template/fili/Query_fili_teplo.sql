With Korp as (SELECT 
  objects.name, 
  objects.guid_parent, 
  objects.guid
FROM 
  public.objects
WHERE 
  objects.name LIKE '%Корпус%Вода%'
  )
SELECT 
  meters.guid as meters_guid, 
  meters.name as meters_name, 
  meters.dt_install, 
  abonents.name as ab_name, 
 objects.guid_parent,
  Korp.name as korp_name,
  objects.name as obj_name, 
  objects.guid as obj_guid
FROM 
  Korp,
  public.meters, 
  public.abonents, 
  public.objects, 
  public.taken_params, 
  public.link_abonents_taken_params, 
  public.types_meters
WHERE 
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid_objects = objects.guid AND
  objects.guid_parent=Korp.guid and
  taken_params.guid_meters = meters.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid
  and  types_meters.name like '%Пульсар%'
  order by Korp.name, objects.name, abonents.name ASC
