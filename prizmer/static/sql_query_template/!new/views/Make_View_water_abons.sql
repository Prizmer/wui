-- View: water_abons

-- DROP VIEW water_abons;

CREATE OR REPLACE VIEW water_abons AS 
 SELECT z1.ab_guid,
    z1.ab_name,
    z1.obj_name,
    z1.factory_number_manual,
    z1.meter_guid,
    z1.name,
    z1.attr2,
    z1.res,
    z1.type_res,
    z1.channel
   FROM (( SELECT abonents.guid AS ab_guid,
            abonents.name AS ab_name,
            objects.name AS obj_name,
            meters.factory_number_manual,
            meters.guid AS meter_guid,
            resources.name as res,
            meters.attr2,
            types_meters.name,
            'ГВ'::text as type_res,
            channel           
           FROM abonents,
            objects,
            link_abonents_taken_params,
            taken_params,
            params,
            meters,
            names_params,
            resources,
            types_meters
          WHERE types_meters.guid=meters.guid_types_meters and
          abonents.guid_objects::text = objects.guid::text AND link_abonents_taken_params.guid_abonents::text = abonents.guid::text 
          AND link_abonents_taken_params.guid_taken_params::text = taken_params.guid::text AND taken_params.guid_params::text = params.guid::text 
          AND taken_params.guid_meters::text = meters.guid::text AND params.guid_names_params::text = names_params.guid::text 
          AND names_params.guid_resources::text = resources.guid::text AND resources.name::text = 'Импульс'::text
          and channel=2
          GROUP BY abonents.guid, abonents.name, objects.name, meters.factory_number_manual, meters.guid, resources.name, meters.attr1, 
            types_meters.name, params.channel
          ORDER BY abonents.name, objects.name, meters.factory_number_manual)
        UNION
        ( SELECT abonents.guid AS ab_guid,
            abonents.name AS ab_name,
            objects.name AS obj_name,
            meters.factory_number_manual,
            meters.guid AS meter_guid,
            resources.name,
            meters.attr1,
            types_meters.name,            
            'ХВ'::text  as type_res,
            channel
           FROM abonents,
            objects,
            link_abonents_taken_params,
            taken_params,
            params,
            meters,
            names_params,
            resources,
            types_meters
          WHERE types_meters.guid=meters.guid_types_meters and
          abonents.guid_objects::text = objects.guid::text AND link_abonents_taken_params.guid_abonents::text = abonents.guid::text 
          AND link_abonents_taken_params.guid_taken_params::text = taken_params.guid::text AND taken_params.guid_params::text = params.guid::text 
          AND taken_params.guid_meters::text = meters.guid::text AND params.guid_names_params::text = names_params.guid::text 
          AND names_params.guid_resources::text = resources.guid::text AND resources.name::text = 'Импульс'::text
          and channel=1
          GROUP BY abonents.guid, abonents.name, objects.name, meters.factory_number_manual, meters.guid, resources.name, meters.attr2, 
            types_meters.name, params.channel
          ORDER BY abonents.name, objects.name, meters.factory_number_manual)) z1
  ORDER BY z1.ab_name, z1.obj_name;

--ALTER TABLE water_abons
--  OWNER TO postgres;
