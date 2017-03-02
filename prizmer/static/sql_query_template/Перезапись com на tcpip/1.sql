SELECT 
  meters.guid as guid_meters, 
  meters.name as name_meters, 
  link_meters_tcpip_settings.guid as guid_link_tcpip, 
  tcpip_settings.guid as guid_tcpip, 
  tcpip_settings.ip_address,
  tcpip_settings.ip_port

FROM 
  public.link_meters_tcpip_settings, 
  public.tcpip_settings, 
  public.meters
WHERE 
  link_meters_tcpip_settings.guid_meters = meters.guid AND
  link_meters_tcpip_settings.guid_tcpip_settings = tcpip_settings.guid and 
  ip_port=1