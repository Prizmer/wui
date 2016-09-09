SELECT 
current_values.date,                           
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = 'Энергия' then current_values.value else null end) as energy,
                          sum(Case when names_params.name = 'Объем' then current_values.value else null end) as volume,
                          sum(Case when names_params.name = 'ElfTon' then current_values.value else null end) as elfTon,
                          sum(Case when names_params.name = 'Ti' then current_values.value else null end) as ti,
                          sum(Case when names_params.name = 'To' then current_values.value else null end) as t0,
                          sum(Case when names_params.name = 'ElfErr' then current_values.value else null end) as elfErr
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.current_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  current_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  abonents.name = 'Квартира 001' AND 
  objects.name = 'Корпус Б' AND 
  types_meters.name = 'Эльф 1.08'
  and current_values.date='29.08.2016'
  group by current_values.date, objects.name,abonents.name, meters.factory_number_manual