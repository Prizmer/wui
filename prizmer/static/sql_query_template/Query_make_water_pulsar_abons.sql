CREATE OR REPLACE VIEW water_pulsar_abons AS 
 SELECT objects.guid AS obj_guid, objects.name AS obj_name, 
    abonents.guid AS ab_guid, abonents.name AS ab_name, 
    meters.name AS meter_name, meters.factory_number_manual, types_meters.name,   
    substring(types_meters.name from 9 for 11) as type_meter,   
    meters.attr1
   FROM abonents, objects, link_abonents_taken_params, taken_params, meters, 
    types_meters
  WHERE abonents.guid_objects::text = objects.guid::text AND link_abonents_taken_params.guid_abonents::text = abonents.guid::text AND link_abonents_taken_params.guid_taken_params::text = taken_params.guid::text AND taken_params.guid_meters::text = meters.guid::text AND meters.guid_types_meters::text = types_meters.guid::text AND (types_meters.name::text = 'Пульсар ГВС'::text OR types_meters.name::text = 'Пульсар ХВС'::text);

ALTER TABLE water_pulsar_abons
  OWNER TO postgres;