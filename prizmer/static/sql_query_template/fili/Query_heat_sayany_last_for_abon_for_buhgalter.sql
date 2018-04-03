SELECT 
  account_2, 
  '2015-01-01'::date AS date_install,
  factory_number_manual,
  'Отопление'::text AS type_energo,
  meters.name,
  daily_values.value ,
  daily_values.date, 
  substring(abonents.name from 10 for char_length(abonents.name)), 
  objects.name
 
 
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
  objects.name = 'Корпус 1А' AND 
  types_meters.name = 'Sayany' AND 
  abonents.account_2 = '5501001' and
   names_params.name = 'Q Система1' 
   and (daily_values.date='03.04.2018'::date-interval '1 day'
   or daily_values.date='03.04.2018'::date-interval '2 day'
   or daily_values.date='03.04.2018'::date-interval '3 day')
  
 order by daily_values.date DESC