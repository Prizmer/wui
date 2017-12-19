SELECT 
  objects.name, 
  abonents.name,   
  names_params.name,  
  sum(Case when (various_values."time">='00:00:00' and various_values."time"<='00:30:00') then various_values.value end)/2 as t0,
  sum(Case when (various_values."time">='01:00' and various_values."time"<='01:30') then various_values.value end)/2 as t1,
  sum(Case when (various_values."time">='02:00' and various_values."time"<='02:30') then various_values.value end)/2 as t2,
  sum(Case when (various_values."time">='03:00' and various_values."time"<='03:30') then various_values.value end)/2 as t3,
  sum(Case when (various_values."time">='04:00' and various_values."time"<='04:30') then various_values.value end)/2 as t4,
  sum(Case when (various_values."time">='05:00' and various_values."time"<='05:30') then various_values.value end)/2 as t5,
  sum(Case when (various_values."time">='06:00' and various_values."time"<='06:30') then various_values.value end)/2 as t6,
  sum(Case when (various_values."time">='07:00' and various_values."time"<='07:30') then various_values.value end)/2 as t7,
  sum(Case when (various_values."time">='08:00' and various_values."time"<='08:30') then various_values.value end)/2 as t8,
  sum(Case when (various_values."time">='09:00' and various_values."time"<='09:30') then various_values.value end)/2 as t9,
  sum(Case when (various_values."time">='10:00' and various_values."time"<='10:30') then various_values.value end)/2 as t10,
  sum(Case when (various_values."time">='11:00' and various_values."time"<='11:30') then various_values.value end)/2 as t11,
  sum(Case when (various_values."time">='12:00' and various_values."time"<='12:30') then various_values.value end)/2 as t12,
    sum(Case when (various_values."time">='13:00' and various_values."time"<='13:30') then various_values.value end)/2 as t13,
  sum(Case when (various_values."time">='14:00' and various_values."time"<='14:30') then various_values.value end)/2 as t14,
  sum(Case when (various_values."time">='15:00' and various_values."time"<='15:30') then various_values.value end)/2 as t15,
  sum(Case when (various_values."time">='16:00' and various_values."time"<='16:30') then various_values.value end)/2 as t16,
  sum(Case when (various_values."time">='17:00' and various_values."time"<='17:30') then various_values.value end)/2 as t17,
  sum(Case when (various_values."time">='18:00' and various_values."time"<='18:30') then various_values.value end)/2 as t18,
  sum(Case when (various_values."time">='19:00' and various_values."time"<='19:30') then various_values.value end)/2 as t19,
  sum(Case when (various_values."time">='20:00' and various_values."time"<='20:30') then various_values.value end)/2 as t20,
  sum(Case when (various_values."time">='21:00' and various_values."time"<='21:30') then various_values.value end)/2 as t21,
  sum(Case when (various_values."time">='22:00' and various_values."time"<='22:30') then various_values.value end)/2 as t22,
  sum(Case when (various_values."time">='23:00' and various_values."time"<='23:30') then various_values.value end)/2 as t23
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
  names_params.name = 'A+ Профиль' and
  abonents.name='Эл.щит. ГРЩ 31632596'

  group by   objects.name, 
  abonents.name,   
  names_params.name

