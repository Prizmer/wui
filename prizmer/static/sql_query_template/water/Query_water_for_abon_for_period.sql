Select z1.ab_name, z1.obj_name, z1.date_start, z1.hvs_start,z1.gvs_start, z2.date_end,z2.hvs_end,z2.gvs_end
from

(SELECT 
  daily_values.date as date_start,
  objects.name as obj_name, 
  abonents.name as ab_name, 
  meters.factory_number_manual as num_factory,  
   sum(Case when names_params.name = 'Канал 1' then daily_values.value else null end) as hvs_start,
   sum(Case when names_params.name = 'Канал 2' then daily_values.value else null end) as gvs_start
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
  abonents.name='Квартира 002' and
  daily_values.date ='06.09.2016'
  group by   objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  daily_values.date) z1,
  (SELECT 
  daily_values.date as date_end,
  objects.name as obj_name, 
  abonents.name as ab_name, 
  meters.factory_number_manual as num_factory,  
   sum(Case when names_params.name = 'Канал 1' then daily_values.value else null end) as hvs_end,
   sum(Case when names_params.name = 'Канал 2' then daily_values.value else null end) as gvs_end
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
  abonents.name='Квартира 002' and
  daily_values.date ='08.09.2016'
  group by   objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  daily_values.date
) z2
where z1.ab_name=z2.ab_name

  
  
