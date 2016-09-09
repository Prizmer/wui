CREATE VIEW electric_groups
          AS
SELECT 
 balance_groups.guid, 
 balance_groups.name as name_group, 
 abonents.name as name_abonents, 
 meters.factory_number_manual as number_manual,
 resources.name
FROM 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters, 
  public.link_balance_groups_meters, 
  public.balance_groups,
  public.names_params,
  public.params,
  public.resources
WHERE 
  taken_params.guid = link_abonents_taken_params.guid_taken_params AND 
  abonents.guid = link_abonents_taken_params.guid_abonents  AND 
  taken_params.guid_params = params.guid AND 
  names_params.guid = params.guid_names_params AND
  taken_params.guid_meters = meters.guid AND 
  meters.guid=link_balance_groups_meters.guid_meters AND
  balance_groups.guid=link_balance_groups_meters.guid_balance_groups AND
  resources.name='Электричество'
 group by  balance_groups.guid, 
 balance_groups.name , 
 abonents.name, 
 meters.factory_number_manual,
 resources.name
 order by  balance_groups.name, abonents.name ASC