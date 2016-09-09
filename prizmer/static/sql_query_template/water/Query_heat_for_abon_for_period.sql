select z1.ab_name, z1.factory_number_manual,z1.energy, z2.energy, z2.energy-z1.energy as delta
from
(SELECT 
daily_values.date,   
                        
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          daily_values.value as energy                   
                                                    
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
  abonents.name = 'Квартира 001' AND 
  objects.name = 'Корпус Б' AND 
  daily_values.date= '01.08.2016' and
  names_params.name='Энергия'
  order by  daily_values.value ASC
  Limit 1) z1,
  (SELECT 
daily_values.date,   
                        
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          daily_values.value as energy                   
                                                    
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
  abonents.name = 'Квартира 001' AND 
  objects.name = 'Корпус Б' AND 
  daily_values.date= '28.08.2016' and
  names_params.name='Энергия'
  order by  daily_values.value ASC
  Limit 1) z2
  where z1.ab_name=z2.ab_name
  