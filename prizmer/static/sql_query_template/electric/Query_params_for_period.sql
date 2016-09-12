Select z3.ab_name, z3.factory_number_manual,
z3.t0_start, z3.t1_start, z3.t2_start, z3.t3_start, z3.t4_start, 
z4.t0_end, z4.t1_end, z4.t2_end, z4.t3_end, z4.t4_end,  
z4.t0_end-z3.t0_start as delta_t0, z4.t1_end-z3.t1_start as delta_t1, z4.t2_end-z3.t2_start as delta_t2, z4.t3_end-z3.t3_start as delta_t3, z4.t4_end-z3.t4_start as delta_t4,
z3.t0R_start, z4.t0R_end,  z4.t0R_end-z3.t0R_start as delta_t0R, z4.ktt,
z4.ktt*z4.ktn*(z4.t0_end-z3.t0_start), z4.ktt*z4.ktn*(z4.t0R_end-z3.t0R_start), z4.ktn, z4.a
from
(Select z2.ktt, z2.ktn, z2.a,z2.date as date_start, electric_abons.obj_name, electric_abons.ab_name, electric_abons.factory_number_manual, z2.name_res, z2.t0 as t0_end, z2.t1 as t1_end, z2.t2 as t2_end, z2.t3 as t3_end, z2.t4 as t4_end, z2.t0r as t0r_end
from electric_abons
Left join
(SELECT z1.ktt, z1.ktn,z1.a,z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
sum(Case when z1.params_name = 'T0 A+' then z1.value else null end) as t0,
sum(Case when z1.params_name = 'T1 A+' then z1.value else null end) as t1,
sum(Case when z1.params_name = 'T2 A+' then z1.value else null end) as t2,
sum(Case when z1.params_name = 'T3 A+' then z1.value else null end) as t3,
sum(Case when z1.params_name = 'T4 A+' then z1.value else null end) as t4,
sum(Case when z1.params_name = 'T0 R+' then z1.value else null end) as t0R
                        FROM
                        (
                                SELECT 
                                  link_abonents_taken_params.coefficient_2 as ktn,
                                  link_abonents_taken_params.coefficient as ktt,
                                  link_abonents_taken_params.coefficient_3 as a,
                                  daily_values.date,    
                                  daily_values.value,                            
                                  abonents.name, 
                                  daily_values.id_taken_params, 
                                  objects.name as name_objects,
                                  names_params.name as params_name,
                                  meters.factory_number_manual as num_manual, 
                                  resources.name as name_res
                                FROM 
                                  public.daily_values, 
                                  public.link_abonents_taken_params, 
                                  public.taken_params, 
                                  public.abonents, 
                                  public.objects, 
                                  public.names_params, 
                                  public.params, 
                                  public.meters, 
                                  public.resources
                                WHERE 
                                  taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                  taken_params.id = daily_values.id_taken_params AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  abonents.guid = link_abonents_taken_params.guid_abonents AND
                                  objects.guid = abonents.guid_objects AND
                                  names_params.guid = params.guid_names_params AND
                                  resources.guid = names_params.guid_resources AND                                  
                                  objects.name = 'Корпус Б' AND 
                                  abonents.name='ВРУ-1 АВР' and
                                  daily_values.date = '28.08.2016' AND 
                                  resources.name = 'Электричество'
                                  ) z1                       
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res, z1.ktt, z1.ktn, z1.a
                      order by z1.name) z2
on electric_abons.ab_name=z2.name_abonent
where electric_abons.obj_name='Корпус Б') z4, 


(Select z2.date as date_start, electric_abons.obj_name, electric_abons.ab_name, electric_abons.factory_number_manual, z2.name_res, z2.t0 as t0_start, z2.t1 as t1_start, z2.t2 as t2_start, z2.t3 as t3_start, z2.t4 as t4_start, z2.t0r as t0r_start
from electric_abons
Left join
(SELECT z1.date, z1.name_objects, z1.name as name_abonent, z1.num_manual, z1.name_res,
sum(Case when z1.params_name = 'T0 A+' then z1.value else null end) as t0,
sum(Case when z1.params_name = 'T1 A+' then z1.value else null end) as t1,
sum(Case when z1.params_name = 'T2 A+' then z1.value else null end) as t2,
sum(Case when z1.params_name = 'T3 A+' then z1.value else null end) as t3,
sum(Case when z1.params_name = 'T4 A+' then z1.value else null end) as t4,
sum(Case when z1.params_name = 'T0 R+' then z1.value else null end) as t0R

                        FROM
                        (
SELECT 
                                  daily_values.date,    
                                  daily_values.value,                            
                                  abonents.name, 
                                  daily_values.id_taken_params, 
                                  objects.name as name_objects,
                                  names_params.name as params_name,
                                  meters.factory_number_manual as num_manual, 
                                  resources.name as name_res
                                FROM 
                                  public.daily_values, 
                                  public.link_abonents_taken_params, 
                                  public.taken_params, 
                                  public.abonents, 
                                  public.objects, 
                                  public.names_params, 
                                  public.params, 
                                  public.meters, 
                                  public.resources
                                WHERE 
                                  taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                                  taken_params.id = daily_values.id_taken_params AND
                                  taken_params.guid_params = params.guid AND
                                  taken_params.guid_meters = meters.guid AND
                                  abonents.guid = link_abonents_taken_params.guid_abonents AND
                                  objects.guid = abonents.guid_objects AND
                                  names_params.guid = params.guid_names_params AND
                                  resources.guid = names_params.guid_resources AND                                  
                                  objects.name = 'Корпус Б' AND 
                                  abonents.name='ВРУ-1 АВР' and
                                  daily_values.date = '25.08.2016' AND 
                                  resources.name = 'Электричество'
                                  ) z1                       
                      group by z1.name, z1.date, z1.name_objects, z1.name, z1.num_manual, z1.name_res
                      order by z1.name) z2
on electric_abons.ab_name=z2.name_abonent
where electric_abons.obj_name='Корпус Б') z3
where z3.ab_name=z4.ab_name and z3.ab_name='ВРУ-1 АВР'