Create View electric_abons_without_sum_report as
SELECT 
  electric_abons_report.account_2, 
  electric_abons_report.date_install, 
  electric_abons_report.name_meter, 
  electric_abons_report.type_energo, 
  electric_abons_report.ab_name, 
  electric_abons_report.obj_name, 
  electric_abons_report.name_params, 
  electric_abons_report.factory_number_manual
FROM 
  public.electric_abons_report
WHERE 
  electric_abons_report.type_energo != 'Электричество'
order by electric_abons_report.account_2,electric_abons_report.obj_name,electric_abons_report.ab_name 