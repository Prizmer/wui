SELECT 
                          abonents.name, 
                          meters.name, 
                          daily_values.value, 
                          daily_values.date,
                          abonents.account_2,
                          params.name,
                          names_params.name,
                          resources.name
                        FROM 
                          public.daily_values, 
                          public.taken_params, 
                          public.meters, 
                          public.params, 
                          public.abonents, 
                          public.link_abonents_taken_params,
                          names_params,
                          resources
                        WHERE 
                          resources.guid=names_params.guid_resources and
                          names_params.guid=params.guid_names_params and
                          daily_values.id_taken_params = taken_params.id AND
                          taken_params.guid_meters = meters.guid AND
                          params.guid = taken_params.guid_params AND
                          link_abonents_taken_params.guid_abonents = abonents.guid AND
                          link_abonents_taken_params.guid_taken_params = taken_params.guid AND
                          abonents.name = 'Квартира 004' AND 
                          daily_values.date = '03.09.2016'