Select z1.name_abonents, z1.number_manual,z1.energy as energy_start, z2.energy as energy_end,z1.energy-z2.energy as delta_energy, z1.volume as volume_start, z2.volume as volume_end, z1.volume-z2.volume as delta_volume
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
            			  abonents.name = 'Квартира 005' and 
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
            			  abonents.name = 'Квартира 005' and 
            			  types_meters.name = 'Пульсар Теплосчётчик' AND 
            			  daily_values.date = '13.08.2017'                                                      
                                  
            group by daily_values.date, 
            			  objects.name, 
            			  abonents.name,             			
            			  meters.factory_number_manual,
            			  types_meters.name
)as z2
where z1.number_manual=z2.number_manual