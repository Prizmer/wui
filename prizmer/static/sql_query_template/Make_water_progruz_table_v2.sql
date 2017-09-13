Select water_abons_report.name, water_abons_report.obj_name,z1.name_meter, z1.name_puls, z1.param_address,z1.address, z1.type_meter, z1.ip_address, z1.ip_port
from water_abons_report
left join
(SELECT 
  water_abons_report.name, 
  water_abons_report.obj_name, 
  abonents.name as name_meter, 
  meters.name as name_puls, 
  params.param_address, 
  meters.address, 
  types_meters.name as type_meter, 
  tcpip_settings.ip_address, 
  tcpip_settings.ip_port
FROM 
  public.water_abons_report, 
  public.abonents, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.meters, 
  public.params, 
  public.types_meters, 
  public.link_meters_tcpip_settings, 
  public.tcpip_settings
WHERE 
  water_abons_report.ab_name = abonents.name AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  meters.guid_types_meters = types_meters.guid AND
  meters.guid = link_meters_tcpip_settings.guid_meters AND
  link_meters_tcpip_settings.guid_tcpip_settings = tcpip_settings.guid
ORDER BY
  water_abons_report.name ASC, 
  water_abons_report.obj_name ASC) as z1
on water_abons_report.ab_name=z1.name_meter
group by water_abons_report.name, water_abons_report.obj_name,z1.name_meter, z1.name_puls, z1.param_address,z1.address, z1.type_meter,z1.ip_address, z1.ip_port
order by water_abons_report.name, water_abons_report.obj_name,z1.param_address
