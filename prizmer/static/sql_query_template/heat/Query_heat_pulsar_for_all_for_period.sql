Select  heat_abons.ab_name, heat_abons.factory_number_manual, 
round((z5.energy_start)::numeric,7) as energy_st,  
round(z5.energy_end::numeric,7)as energy_e, 
round((z5.energy_end-z5.energy_start)::numeric,7) as energy_delta, 
round((z5.volume_start)::numeric,7), 
round((z5.volume_end)::numeric,7), 
round((z5.volume_end-z5.volume_start)::numeric,7) as volume_delta

 
from heat_abons
left join

(Select z3.obj_name, z3.ab_name,z3.factory_number_manual, z3.energy_start,z3.volume_start , z4.energy_end,z4.volume_end
from
(Select z2.daily_date, heat_abons.obj_name, heat_abons.ab_name, heat_abons.factory_number_manual, z2.energy as energy_start,z2.volume as volume_start,z2.t_in as t_in_start,z2.t_out as t_out_start
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
            			  daily_values.date = '28.11.2017' 
                                    ) z1
            group by z1.name_abonents, z1.daily_date, z1.name_objects, z1.number_manual
            order by z1.name_abonents) as z2
on z2.number_manual=heat_abons.factory_number_manual
where heat_abons.obj_name='Корпус C1') as z3,
(Select z2.daily_date, heat_abons.obj_name, heat_abons.ab_name, heat_abons.factory_number_manual, z2.energy as energy_end,z2.volume as volume_end,z2.t_in as t_in_end,z2.t_out as t_out_end
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
where heat_abons.obj_name='Корпус C1') as z4
where z3.factory_number_manual=z4.factory_number_manual
) as z5
on z5.factory_number_manual=heat_abons.factory_number_manual
where heat_abons.obj_name='Корпус C1' 
order by heat_abons.ab_name