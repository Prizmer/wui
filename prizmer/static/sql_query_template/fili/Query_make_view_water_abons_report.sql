Create view water_abons_report as
(
With Korp as (SELECT 
  objects.name, 
  objects.guid_parent, 
  objects.guid
FROM 
  public.objects
WHERE 
  objects.name LIKE '%Корпус%Вода%'
  )
SELECT 
  Korp.name,
  abonents.account_2,   
  abonents.name as ab_name,
  case when abonents.name like '%ГВС%' then 'Горячее водоснабжение' else 'Холодное водоснабжение' end as type_energo,
  '01.01.2015'::date as date_install,  
  objects.name as obj_name
FROM 
  Korp,
  public.meters, 
  public.abonents, 
  public.objects, 
  public.taken_params, 
  public.link_abonents_taken_params, 
  public.types_meters
WHERE 
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid_objects = objects.guid AND
  objects.guid_parent=Korp.guid and
  taken_params.guid_meters = meters.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid
  and  types_meters.name like '%Пульсар%'
  order by Korp.name, objects.name, abonents.name ASC
)