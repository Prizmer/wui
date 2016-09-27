Select heat_abons.ab_name,heat_abons.factory_number_manual, z3.energy, z3.energy2, z3.delta
from heat_abons
left join 
(select z1.ab_name, z1.factory_number_manual,z1.energy, z2.energy as energy2, z2.energy-z1.energy as delta
from
(SELECT 
daily_values.date,   
                        
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          daily_values.value as energy                   
                                                    
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND

  objects.name = 'Корпус 2' AND 
  daily_values.date= '10.09.2016' and
  names_params.name='Энергия'
  order by  daily_values.value ASC
  ) z1,
  (SELECT 
daily_values.date,   
                        
                          objects.name, 
                          abonents.name as ab_name, 
                          meters.factory_number_manual,                           
                          daily_values.value as energy                   
                                                    
FROM 
  public.link_abonents_taken_params, 
  public.meters, 
  public.abonents, 
  public.taken_params, 
  public.objects, 
  public.daily_values, 
  public.params, 
  public.names_params, 
  public.types_meters
WHERE 
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  meters.guid = taken_params.guid_meters AND
  meters.guid_types_meters = types_meters.guid AND
  abonents.guid = link_abonents_taken_params.guid_abonents AND
  abonents.guid_objects = objects.guid AND
  taken_params.guid_params = params.guid AND
  daily_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  params.guid_types_meters = types_meters.guid AND

  objects.name = 'Корпус 2' AND 
  daily_values.date= '09.09.2016' and
  names_params.name='Энергия'
  order by  daily_values.value ASC
  ) z2
  where z1.ab_name=z2.ab_name) z3
  on heat_abons.ab_name=z3.ab_name
  where heat_abons.obj_name='Корпус 2'
  order by heat_abons.ab_name