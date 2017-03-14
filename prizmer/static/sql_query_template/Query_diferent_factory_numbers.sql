SELECT 
  objects.name as obj_name, 
  abonents.name as ab_name, 
  meters.name as meter_name, 
  meters.factory_number_manual, 
  meters.factory_number_readed, 
  meters.is_factory_numbers_equal, 
  meters.dt_last_read, 
  resources.name as res_name
FROM 
  public.meters, 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid AND
  names_params.guid_resources = resources.guid and
  is_factory_numbers_equal= False and
  resources.name='Электричество'
group by     
objects.name, 
  abonents.name, 
  meters.name, 
  meters.factory_number_manual, 
  meters.factory_number_readed, 
  meters.is_factory_numbers_equal, 
  meters.dt_last_read, 
  resources.name
