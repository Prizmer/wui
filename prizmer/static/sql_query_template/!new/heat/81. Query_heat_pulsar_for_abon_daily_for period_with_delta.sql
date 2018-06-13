Select z3.c_date,z3.name_abonents,z3.name_objects, z3.number_manual, z3.energy,z3.volume,
round((z3.energy-lag(energy)over (order by c_date))::numeric,3)  as delta_energy,
round((z3.volume-lag(volume) over (order by c_date))::numeric,3) as delta_volume
from
(
Select *
from
(select c_date::date
from
generate_series('01.06.2018'::timestamp without time zone, '06.06.2018'::timestamp without time zone, interval '1 day') as c_date) z_date
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
            			  objects.name = 'Лазоревый пр-д, д.1а к2 (к6)' AND
            			  abonents.name = 'Квартира 005' and 
            			  types_meters.name = 'Пульсар Теплосчётчик' AND 
            			  daily_values.date between '04.06.2018' and '06.06.2018'
                                    ) z1                      
group by z1.name_abonents, z1.daily_date, z1.name_objects, z1.number_manual
order by z1.name_abonents) z2
on z2.daily_date=z_date.c_date
 order by z_date.c_date) z3