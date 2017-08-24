﻿SELECT 
  daily_values.date,  
  abonents.name, 
  substring(types_meters.name from 9 for 11),
   
  meters.attr1,
  meters.factory_number_manual,   
  daily_values.value,   
  abonents.guid
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.daily_values, 
  public.meters, 
  public.types_meters
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid AND
  objects.name = 'Корпус 2' AND 
  abonents.name='Квартира 002' and
  daily_values.date = '11.08.2017' and
  (types_meters.name='Пульсар ХВС' or types_meters.name='Пульсар ГВС')
ORDER BY
  abonents.name ASC;
