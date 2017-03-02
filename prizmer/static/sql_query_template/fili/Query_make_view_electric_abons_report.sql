/*Drop view if exists electric_abons_report*/
Create view electric_abons_report
as
SELECT 
  abonents.account_2,
  '01/01/2015'::date as date_install,
  meters.name as name_meter,
  case when names_params.name like '%T0%' then 'Электричество Сумма' 
       when names_params.name like '%T1%' then 'Электричество Тариф 1' 
       when names_params.name like '%T2%' then 'Электричество Тариф 2' 
       when names_params.name like '%T3%' then 'Электричество Тариф 3' 
       else 'Электричество' end as type_energo,
  
  abonents.name as ab_name, 
  objects.name as obj_name,  
  names_params.name as name_params
  
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid AND
  meters.name LIKE '%М-230%' 
  group by  abonents.account_2,
  meters.name,
  abonents.name, 
  objects.name,  
  names_params.name
  order by objects.name,abonents.name, abonents.account_2