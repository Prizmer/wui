Select heat_abons.ab_name, heat_abons.factory_number_manual, z3.energy_start, z3.energy_end, z3.energy_start-z3.energy_end as delta_energy, z3.volume_start, z3.volume_end,z3.volume_start-z3.volume_end as delta_volume
from heat_abons
inner join
(Select z1.name_abonents, z1.number_manual,z1.energy as energy_start, z2.energy as energy_end, z1.volume as volume_start, z2.volume as volume_end
from
(SELECT 
            			  objects.name as name_objects, 
            			  abonents.name as name_abonents,            			 
            			  meters.factory_number_manual as number_manual, 
            sum(Case when names_params.name = 'Энергия' then daily_values.value  end) as energy,
            sum(Case when names_params.name = 'Объем' then daily_values.value  end) as volume,
            sum(Case when names_params.name = 'Ti' then daily_values.value  end) as t_in,
            sum(Case when names_params.name = 'To' then daily_values.value  end) as t_out,
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
            			  objects.name = 'Корпус 2' AND
            			  
            			  types_meters.name = 'Пульсар Теплосчётчик' AND 
            			  daily_values.date = '11.08.2017'                                                      
                                  
            group by daily_values.date, 
            			  objects.name, 
            			  abonents.name,             			
            			  meters.factory_number_manual,
            			  types_meters.name )as z1,

(SELECT 
            			  objects.name as name_objects, 
            			  abonents.name as name_abonents,            			 
            			  meters.factory_number_manual as number_manual, 
            sum(Case when names_params.name = 'Энергия' then daily_values.value  end) as energy,
            sum(Case when names_params.name = 'Объем' then daily_values.value  end) as volume,
            sum(Case when names_params.name = 'Ti' then daily_values.value  end) as t_in,
            sum(Case when names_params.name = 'To' then daily_values.value  end) as t_out,
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
            			  objects.name = 'Корпус 2' AND
            			  
            			  types_meters.name = 'Пульсар Теплосчётчик' AND 
            			  daily_values.date = '13.08.2017'                                                      
                                  
            group by daily_values.date, 
            			  objects.name, 
            			  abonents.name,             			
            			  meters.factory_number_manual,
            			  types_meters.name
)as z2
where z1.number_manual=z2.number_manual) as z3
on z3.number_manual=heat_abons.factory_number_manual
where heat_abons.obj_name='Корпус 2' 