create view  VRU_no_ITP as
SELECT 
  abonents.name as ab_name,
   abonents.guid as ab_guid, 
  objects.name as obj_name, 
  meters.name as meter, 
  meters.factory_number_manual
FROM 
  public.objects, 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid and
  abonents.name like 'ВРУ%' and
  abonents.name not like '%ИТП%' 

  group by  abonents.name, 
  objects.name, 
  meters.name, 
  meters.factory_number_manual, abonents.guid
  order by  abonents.name,  objects.name
