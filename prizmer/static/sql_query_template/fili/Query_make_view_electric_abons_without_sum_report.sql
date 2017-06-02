﻿ SELECT electric_abons_report.account_2, electric_abons_report.date_install, 
    electric_abons_report.name_meter, electric_abons_report.type_energo, 
    electric_abons_report.ab_name, electric_abons_report.obj_name, 
    electric_abons_report.name_params, 
    electric_abons_report.factory_number_manual, 
    (electric_abons_report.name_meter::text || '-'::text) || "substring"(electric_abons_report.type_energo, char_length(electric_abons_report.type_energo), char_length(electric_abons_report.type_energo)) AS report_factory_number_manual
   FROM electric_abons_report
  WHERE electric_abons_report.type_energo <> 'Электричество'::text
  ORDER BY electric_abons_report.account_2, electric_abons_report.obj_name, electric_abons_report.ab_name;
