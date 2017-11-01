CREATE OR REPLACE VIEW electric_progruz AS 
SELECT 
  abonents.guid as ab_guid,
  objects.name as obj_name, 
  abonents.name as ab_name, 
  ''::text as askue,
  ''::text as numLic, 
  meters.factory_number_manual, 
  meters.address, 
  types_meters.name as type_meter, 
  link_abonents_taken_params.coefficient, 
  tcpip_settings.ip_address, 
  tcpip_settings.ip_port
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters, 
  public.tcpip_settings, 
  public.link_meters_tcpip_settings, 
  public.types_meters, 
  public.params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  link_meters_tcpip_settings.guid_meters = meters.guid AND
  link_meters_tcpip_settings.guid_tcpip_settings = tcpip_settings.guid AND
  params.guid_types_meters = types_meters.guid and
  types_meters.name='Меркурий 230'
    group by 
    abonents.guid, objects.name, 
  abonents.name, 
  meters.factory_number_manual, 
  meters.address, 
  types_meters.name, 
  link_abonents_taken_params.coefficient, 
  tcpip_settings.ip_address, 
  tcpip_settings.ip_port
  order by 
  
objects.name ,
  abonents.name
