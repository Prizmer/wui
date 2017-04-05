-- View: heat_abons_report

-- DROP VIEW heat_abons_report;

CREATE OR REPLACE VIEW heat_abons_report AS 
 SELECT abonents.account_2, meters.name AS meter_name, 
    'Отопление'::text AS type_energo, 
    '2015-01-01'::date AS date_install, abonents.name AS ab_name, 
    meters.factory_number_manual,
    objects.name as obj_name
   FROM abonents, link_abonents_taken_params, objects, taken_params, meters
  WHERE abonents.guid_objects::text = objects.guid::text AND link_abonents_taken_params.guid_abonents::text = abonents.guid::text AND link_abonents_taken_params.guid_taken_params::text = taken_params.guid::text AND taken_params.guid_meters::text = meters.guid::text AND meters.name::text ~~ '%Sayany%'::text
  GROUP BY abonents.account_2, objects.name, abonents.name, meters.name, meters.factory_number_manual;

ALTER TABLE heat_abons_report
  OWNER TO postgres;

