SELECT 
  daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
sum(Case when names_params.name = 'Q Система1' then daily_values.value  end) as q1,
sum(Case when names_params.name = 'M Система1' then daily_values.value  end) as m1,
sum(Case when names_params.name = 'T Канал1' then daily_values.value  end) as t1,
sum(Case when names_params.name = 'T Канал2' then daily_values.value  end) as t2
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  params.guid_names_params = names_params.guid AND
  objects.name = 'Корпус 2' AND 
  types_meters.name = 'Sayany' AND 
  abonents.name = 'Квартира 0002' AND 
  daily_values.date = '06.12.2016'
  group by daily_values.date, 
  objects.name, 
  abonents.name,   
  meters.factory_number_manual, 
  types_meters.name

  
