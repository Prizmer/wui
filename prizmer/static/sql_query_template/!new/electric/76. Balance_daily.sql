SELECT 
  balance_groups.name,
  types_abonents.name,
  sum(case when link_balance_groups_meters.type=True then (0+daily_values.value * link_abonents_taken_params.coefficient) else (0-daily_values.value * link_abonents_taken_params.coefficient) end), 
  names_params.name, 
  resources.name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.link_balance_groups_meters, 
  public.taken_params, 
  public.meters, 
  public.balance_groups, 
  public.types_abonents, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.resources
WHERE 
  abonents.guid_objects = objects.guid AND
  abonents.guid_types_abonents = types_abonents.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  link_balance_groups_meters.guid_meters = meters.guid AND
  link_balance_groups_meters.guid_balance_groups = balance_groups.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  names_params.guid_resources = resources.guid AND
  balance_groups.name = 'Баланс Корпус 5-1' AND 
  daily_values.date = '25.05.2018' AND 
  names_params.name = 'T0 A+' 
  group by  balance_groups.name, 
    names_params.name, 
  resources.name,
   types_abonents.name
