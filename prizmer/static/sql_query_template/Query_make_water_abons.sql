﻿-- View: water_abons

-- DROP VIEW water_abons;

CREATE OR REPLACE VIEW water_abons AS 
 SELECT abonents.guid AS ab_guid, abonents.name AS ab_name, 
    objects.name AS obj_name, meters.factory_number_manual, resources.name, names_params.name as names_params
   FROM abonents, objects, link_abonents_taken_params, taken_params, params, 
    meters, names_params, resources
  WHERE abonents.guid_objects::text = objects.guid::text AND link_abonents_taken_params.guid_abonents::text = abonents.guid::text AND link_abonents_taken_params.guid_taken_params::text = taken_params.guid::text AND taken_params.guid_params::text = params.guid::text AND taken_params.guid_meters::text = meters.guid::text AND params.guid_names_params::text = names_params.guid::text AND names_params.guid_resources::text = resources.guid::text AND resources.name::text = 'Импульс'::text
  GROUP BY abonents.guid, abonents.name, objects.name, meters.factory_number_manual, resources.name, names_params.name
  ORDER BY abonents.name;

ALTER TABLE water_abons
  OWNER TO postgres;

