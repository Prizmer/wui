SELECT 
  objects.name, 
  abonents.name, 
  taken_params.name, 
  various_values.date, 
  various_values."time", 
  various_values.value, 
  names_params.name
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.various_values, 
  public.params, 
  public.names_params
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  various_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  various_values.date = '01.10.2017' AND 
  names_params.name = 'R+ Профиль' and
  abonents.name='Эл.щит. ГРЩ 31632596'
ORDER BY
  abonents.name ASC, 
  various_values.date ASC, 
  various_values."time" ASC;
