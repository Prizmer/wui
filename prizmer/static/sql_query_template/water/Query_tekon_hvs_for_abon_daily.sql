SELECT 
  daily_values.date,
  abonents.name, 
  meters.factory_number_manual ,
  daily_values.value 
  
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.names_params, 
  public.params, 
  public.resources, 
  public.meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  names_params.guid_resources = resources.guid AND
  params.guid_names_params = names_params.guid
And
   names_params.name='Канал 1' and
   resources.name='Импульс' and
   abonents.name='Квартира 0640' and
   objects.name='Корпус 7' and
   daily_values.date='20.12.2016' ;
    
  
