delete from daily_values
where id in
(
SELECT  
  daily_values.id
FROM 
  public.types_meters, 
  public.taken_params, 
  public.daily_values, 
  public.meters
WHERE 
  taken_params.guid_meters = meters.guid AND
  daily_values.id_taken_params = taken_params.id AND
  meters.guid_types_meters = types_meters.guid
  and meters.name like '%М%230%'
  and date>'27.02.2017'
)
returning *