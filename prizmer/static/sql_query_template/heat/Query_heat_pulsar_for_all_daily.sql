Select z2.daily_date, heat_abons.obj_name, heat_abons.ab_name, heat_abons.factory_number_manual, 
round(z2.energy::numeric,7),
round(z2.volume::numeric,7),
round(z2.t_in::numeric,1),
round(z2.t_out::numeric,1)
from heat_abons
left join
(SELECT z1.daily_date, z1.name_objects, z1.name_abonents, z1.number_manual, 
            sum(Case when z1.params_name = 'Энергия' then z1.value_daily  end) as energy,
            sum(Case when z1.params_name = 'Объем' then z1.value_daily  end) as volume,
            sum(Case when z1.params_name = 'Ti' then z1.value_daily  end) as t_in,
            sum(Case when z1.params_name = 'To' then z1.value_daily  end) as t_out
            
                                    FROM
                                    (SELECT 
            			  daily_values.date as daily_date, 
            			  objects.name as name_objects, 
            			  abonents.name as name_abonents, 
            			  daily_values.value as value_daily, 
            			  meters.factory_number_manual as number_manual, 
            			  names_params.name as params_name, 
            			  types_meters.name as meter_type
            			FROM 
            			  public.daily_values, 
            			  public.taken_params, 
            			  public.abonents, 
            			  public.link_abonents_taken_params, 
            			  public.objects, 
            			  public.params, 
            			  public.names_params, 
            			  public.meters, 
            			  public.types_meters
            			WHERE 
            			  daily_values.id_taken_params = taken_params.id AND
            			  taken_params.guid_params = params.guid AND
            			  taken_params.guid_meters = meters.guid AND
            			  abonents.guid_objects = objects.guid AND
            			  link_abonents_taken_params.guid_abonents = abonents.guid AND
            			  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
            			  params.guid_names_params = names_params.guid AND
            			  meters.guid_types_meters = types_meters.guid AND
            			  objects.name = 'Корпус C1' AND            			  
            			  types_meters.name = 'Пульсар Теплосчётчик' AND 
            			  daily_values.date = '30.11.2017' 
                                    ) z1
            group by z1.name_abonents, z1.daily_date, z1.name_objects, z1.number_manual
            order by z1.name_abonents) as z2
on z2.number_manual=heat_abons.factory_number_manual
where heat_abons.obj_name='Корпус C1'
order by heat_abons.ab_name