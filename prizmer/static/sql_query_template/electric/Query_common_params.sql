SELECT z1.monthly_date, z1.name_objects, z1.name_abonents, z1.number_manual, z1.value_monthly as T0, z2.value_monthly as T1, z3.value_monthly as T2, z4.value_monthly as T3
                        FROM
                        (SELECT monthly_values.date as monthly_date, objects.name as name_objects, abonents.name as name_abonents, meters.factory_number_manual as number_manual, monthly_values.value as value_monthly
                        FROM
                         public.monthly_values, public.link_abonents_taken_params, public.taken_params, public.abonents, public.objects, public.names_params, public.params, public.meters 
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND taken_params.id = monthly_values.id_taken_params AND taken_params.guid_params = params.guid AND taken_params.guid_meters = meters.guid AND abonents.guid = link_abonents_taken_params.guid_abonents AND objects.guid = abonents.guid_objects AND names_params.guid = params.guid_names_params AND
                        abonents.name = 'Квартира 061' AND 
                        objects.name = 'Корпус 5' AND 
                        names_params.name = 'T0 A+' AND 
                        monthly_values.date = '01.06.2016') z1,
                        
                        (SELECT monthly_values.date as monthly_date, objects.name as name_objects, abonents.name as name_abonents, meters.factory_number_manual as number_manual, monthly_values.value as value_monthly
                        FROM
                         public.monthly_values, public.link_abonents_taken_params, public.taken_params, public.abonents, public.objects, public.names_params, public.params, public.meters 
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND taken_params.id = monthly_values.id_taken_params AND taken_params.guid_params = params.guid AND taken_params.guid_meters = meters.guid AND abonents.guid = link_abonents_taken_params.guid_abonents AND objects.guid = abonents.guid_objects AND names_params.guid = params.guid_names_params AND
                        abonents.name = 'Квартира 061' AND 
                        objects.name = 'Корпус 5' AND 
                        names_params.name = 'T1 A+' AND 
                        monthly_values.date = '01.06.2016') z2,

                         (SELECT monthly_values.date as monthly_date, objects.name as name_objects, abonents.name as name_abonents, meters.factory_number_manual as number_manual, monthly_values.value as value_monthly
                        FROM
                         public.monthly_values, public.link_abonents_taken_params, public.taken_params, public.abonents, public.objects, public.names_params, public.params, public.meters 
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND taken_params.id = monthly_values.id_taken_params AND taken_params.guid_params = params.guid AND taken_params.guid_meters = meters.guid AND abonents.guid = link_abonents_taken_params.guid_abonents AND objects.guid = abonents.guid_objects AND names_params.guid = params.guid_names_params AND
                        abonents.name = 'Квартира 061' AND 
                        objects.name = 'Корпус 5' AND 
                        names_params.name = 'T2 A+' AND 
                        monthly_values.date = '01.06.2016') z3,

                         (SELECT monthly_values.date as monthly_date, objects.name as name_objects, abonents.name as name_abonents, meters.factory_number_manual as number_manual, monthly_values.value as value_monthly
                        FROM
                         public.monthly_values, public.link_abonents_taken_params, public.taken_params, public.abonents, public.objects, public.names_params, public.params, public.meters 
                        WHERE
                        taken_params.guid = link_abonents_taken_params.guid_taken_params AND taken_params.id = monthly_values.id_taken_params AND taken_params.guid_params = params.guid AND taken_params.guid_meters = meters.guid AND abonents.guid = link_abonents_taken_params.guid_abonents AND objects.guid = abonents.guid_objects AND names_params.guid = params.guid_names_params AND
                        abonents.name = 'Квартира 061' AND 
                        objects.name = 'Корпус 5' AND 
                        names_params.name = 'T3 A+' AND 
                        monthly_values.date = '01.06.2016') z4


ORDER BY z1.name_objects ASC