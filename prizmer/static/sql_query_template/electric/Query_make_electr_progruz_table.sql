SELECT 
  parent_objects_for_progruz.obj_name2, 
  parent_objects_for_progruz.obj_name1, 
  parent_objects_for_progruz.obj_name0, 
  parent_objects_for_progruz.ab_name, 
  electric_progruz.askue, 
  electric_progruz.numlic, 
  electric_progruz.factory_number_manual, 
  electric_progruz.address, 
  electric_progruz.type_meter, 
  electric_progruz.coefficient, 
  electric_progruz.ip_address, 
  electric_progruz.ip_port
FROM 
  public.electric_progruz, 
  public.parent_objects_for_progruz
WHERE 
  parent_objects_for_progruz.ab_guid = electric_progruz.ab_guid;
