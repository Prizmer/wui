Delete from link_meters_comport_settings
where link_meters_comport_settings.guid in (
SELECT  
  link_meters_comport_settings.guid as guid_link_com
FROM 
  public.link_meters_comport_settings, 
  public.comport_settings, 
  public.meters
WHERE 
  link_meters_comport_settings.guid_meters = meters.guid AND
  link_meters_comport_settings.guid_comport_settings = comport_settings.guid and
  comport_settings.name = '11'
  ) 
  returning link_meters_comport_settings.guid_meters