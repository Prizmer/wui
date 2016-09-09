SELECT 

                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          sum(Case when names_params.name = 'Энергия' then daily_values.value else null end) as energy,
                          sum(Case when names_params.name = 'Объем' then daily_values.value else null end) as volume,
                          sum(Case when names_params.name = 'ElfTon' then daily_values.value else null end) as elfTon                                
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
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
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND
  abonents.name = 'Квартира 004' AND 
  objects.name = 'Корпус 3' AND 
  daily_values.date= '03.09.2016' AND 
  types_meters.name = 'Эльф 1.08'
  group by   abonents.name, meters.factory_number_manual
