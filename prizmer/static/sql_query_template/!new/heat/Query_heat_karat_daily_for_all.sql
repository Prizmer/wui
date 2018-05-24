SELECT 
  objects.name, 
  abonents.name,  
  meters.name,  
  types_meters.name,
  
  sum(Case when names_params.name = 'Q Система1' then daily_values.value  end) as Q,
  sum(Case when names_params.name = 'M Система1' then daily_values.value  end) as M,
sum(Case when names_params.name = 'Ti' then daily_values.value  end) as ti,
sum(Case when names_params.name = 'To' then daily_values.value  end) as to,
sum(Case when names_params.name = 'Ton' then daily_values.value  end) as ton,
sum(Case when names_params.name = 'Terr' then daily_values.value  end) as terr
FROM 
  public.objects, 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.params, 
  public.meters, 
  public.types_params, 
  public.resources, 
  public.names_params, 
  public.types_meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_types_params = types_params.guid AND
  params.guid_names_params = names_params.guid AND
  meters.guid_types_meters = types_meters.guid AND
  names_params.guid_resources = resources.guid AND
  daily_values.date = '24.05.2018' AND 
  types_meters.name = 'Карат 307'
  group by   objects.name, 
  abonents.name,  
  meters.name, 
  types_meters.name
  order by   objects.name, 
  abonents.name
