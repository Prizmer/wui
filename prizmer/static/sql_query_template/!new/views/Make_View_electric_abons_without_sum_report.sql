-- View: electric_abons_without_sum_report

-- DROP VIEW electric_abons_without_sum_report;

CREATE OR REPLACE VIEW electric_abons_without_sum_report AS 
 SELECT electric_abons_report.account_2,
    electric_abons_report.date_install,
    electric_abons_report.name_meter,
    electric_abons_report.type_energo,
    electric_abons_report.ab_name,
    electric_abons_report.obj_name,
    electric_abons_report.name_params,
    electric_abons_report.factory_number_manual,
    electric_abons_report.name_meter::text AS report_factory_number_manual,
    ("substring"(electric_abons_report.name_params::text, 0, 3) || '-'::text) || electric_abons_report.factory_number_manual::text AS report_num_meter
   FROM electric_abons_report
  WHERE electric_abons_report.type_energo <> 'Электричество'::text
  ORDER BY electric_abons_report.account_2, electric_abons_report.obj_name, electric_abons_report.ab_name;

ALTER TABLE electric_abons_without_sum_report
  OWNER TO postgres;
