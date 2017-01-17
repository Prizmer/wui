CREATE EXTENSION IF NOT EXISTS "uuid-ossp"

with free_meters as (
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
  comport_settings.name = '2'
  ) 
  returning link_meters_comport_settings.guid_meters
)
CREATE OR REPLACE VIEW free_meters(guid_meters) as 
    Select * from free_meters

  

with giud_tcp1 as(
INSERT INTO tcpip_settings(
             guid, ip_address, ip_port, write_timeout, read_timeout, attempts, 
            delay_between_sending)
    VALUES ( uuid_generate_v4(), '192.168.23.104', 1, 200, 400, 3,400)
    returning guid
            )

for guid_meter in (select guid_meters from free_meters) loop
    INSERT INTO link_meters_tcpip_settings(
            guid, guid_meters, guid_tcpip_settings)
    VALUES (uuid_generate_v4(), guid_meter, (select guid from giud_tcp1))
End loop;
    )
    )

SELECT 
  meters.guid as guid_meters, 
  meters.name as name_meters, 
  link_meters_comport_settings.guid as guid_link_com, 
  comport_settings.guid as guid_com, 
  comport_settings.name as name_com
FROM 
  public.link_meters_comport_settings, 
  public.comport_settings, 
  public.meters
WHERE 
  link_meters_comport_settings.guid_meters = meters.guid AND
  link_meters_comport_settings.guid_comport_settings = comport_settings.guid and
  comport_settings.name = '2')