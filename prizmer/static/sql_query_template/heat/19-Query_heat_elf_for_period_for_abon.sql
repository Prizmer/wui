Select z_start.obj_name, z_start.ab_name, z_start.factory_number_manual, 
z_start.energy_start, z_end.energy_end, round((z_end.energy_end-z_start.energy_start)::numeric, 2) as energy_delta,
z_start.volume_start, z_end.volume_end, round((z_end.volume_end-z_start.volume_start)::numeric, 2) as volume_delta,
z_start.ton_start, z_end.ton_end, z_end.ton_end-z_start.ton_start as ton_delta
 
from
(Select heat_abons.obj_name, heat_abons.ab_name, z1.energy_start,z1.volume_start, z1.ton_start, heat_abons.factory_number_manual
from
heat_abons
Left Join 
(SELECT 
  objects.name as obj_name, 
  abonents.name as ab_name,  
  daily_values.date as date_start,    
  resources.name,
  sum(Case when names_params.name = 'Энергия' then daily_values.value else null end) as energy_start,
                          sum(Case when names_params.name = 'Объем' then daily_values.value else null end) as volume_start,
                          sum(Case when names_params.name = 'ElfTon' then daily_values.value else null end) as ton_start,
                          sum(Case when names_params.name = 'ElfErr' then daily_values.value else null end) as terr_start   
FROM 
  public.abonents, 
  public.daily_values, 
  public.link_abonents_taken_params, 
  public.objects, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources
WHERE 
  abonents.guid_objects = objects.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid AND
  names_params.guid_resources = resources.guid AND
  daily_values.date = '01/02/2018' AND 
  resources.name = 'Тепло' AND 
  objects.name = 'Корпус Б'
  and abonents.name='Квартира 001'
  group by objects.name, 
  abonents.name,  
  daily_values.date,     
  resources.name
) as z1
on heat_abons.ab_name=z1.ab_name and heat_abons.obj_name=z1.obj_name
where heat_abons.obj_name='Корпус Б' and heat_abons.ab_name='Квартира 001') as z_start,
(Select heat_abons.obj_name, heat_abons.ab_name, z1.energy_end,z1.volume_end, z1.ton_end, heat_abons.factory_number_manual
from
heat_abons
Left Join 
(SELECT 
  objects.name as obj_name, 
  abonents.name as ab_name,  
  daily_values.date as date_start,    
  resources.name,
  sum(Case when names_params.name = 'Энергия' then daily_values.value else null end) as energy_end,
                          sum(Case when names_params.name = 'Объем' then daily_values.value else null end) as volume_end,
                          sum(Case when names_params.name = 'ElfTon' then daily_values.value else null end) as ton_end,
                          sum(Case when names_params.name = 'ElfErr' then daily_values.value else null end) as terr_end   
FROM 
  public.abonents, 
  public.daily_values, 
  public.link_abonents_taken_params, 
  public.objects, 
  public.taken_params, 
  public.params, 
  public.names_params, 
  public.resources
WHERE 
  abonents.guid_objects = objects.guid AND
  daily_values.id_taken_params = taken_params.id AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  params.guid_names_params = names_params.guid AND
  names_params.guid_resources = resources.guid AND
  daily_values.date = '15/02/2018' AND 
  resources.name = 'Тепло' AND 
  objects.name = 'Корпус Б'
  and abonents.name='Квартира 001'
  group by objects.name, 
  abonents.name,  
  daily_values.date,     
  resources.name
) as z1
on heat_abons.ab_name=z1.ab_name and heat_abons.obj_name=z1.obj_name
where heat_abons.obj_name='Корпус Б'  and heat_abons.ab_name='Квартира 001') as z_end

where z_start.ab_name=z_end.ab_name
order by z_start.ab_name