SELECT 
  daily_values.date,

  objects.name, 
  abonents.name, 
  meters.factory_number_manual,  
   sum(Case when names_params.name = 'Канал 1' then daily_values.value else null end) as hvs,
   sum(Case when names_params.name = 'Канал 2' then daily_values.value else null end) as gvs
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources, 
  public.meters, 
  public.types_meters,
  daily_values
WHERE 
daily_values.id_taken_params=taken_params.id and
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  meters.guid_types_meters = types_meters.guid and
  resources.name='Импульс' and
  objects.name='Корпус 3' and
  abonents.name='Квартира 002' 
  group by   objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  daily_values.date 
  order by daily_values.date ASC
  Limit 1
  
  
