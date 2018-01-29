with date_st as (
   SELECT 
  objects.name, 
  abonents.name, 
  names_params.name, 
  various_values.date, 
  various_values."time", 
  various_values.value
FROM 
  public.various_values, 
  public.taken_params, 
  public.link_abonents_taken_params, 
  public.abonents, 
  public.objects, 
  public.meters, 
  public.names_params, 
  public.params
WHERE 
  various_values.id_taken_params = taken_params.id AND
  taken_params.guid_meters = meters.guid AND
  taken_params.guid_params = params.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  abonents.guid_objects = objects.guid AND
  params.guid_names_params = names_params.guid AND
  various_values."time" =  '00:00:00' AND 
  various_values.date = ('01.'::text||(extract(month from timestamp '19.12.2017'))::text||'.'||(extract(year from timestamp '19.12.2017'))::text)::timestamp AND 
  names_params.name = 'R+ Профиль' and
  abonents.name='ГРЩ 1 Ввод2'
  )
  
SELECT 
  date_st.value,
   coefficient as ktt,
   coefficient_2 as ktn, 
   coefficient_3 as A,
  objects.name, 
  abonents.name,   
  names_params.name,  
  sum(Case when (various_values."time">='00:00:00' and various_values."time"<='00:30:00') then various_values.value end)/2 as t0,
  sum(Case when (various_values."time">='01:00' and various_values."time"<='01:30') then various_values.value end)/2 + date_st.value as t1,
  sum(Case when (various_values."time">='02:00' and various_values."time"<='02:30') then various_values.value end)/2 + date_st.value as t2,
  sum(Case when (various_values."time">='03:00' and various_values."time"<='03:30') then various_values.value end)/2 + date_st.value as t3,
  sum(Case when (various_values."time">='04:00' and various_values."time"<='04:30') then various_values.value end)/2 + date_st.value  as t4,
  sum(Case when (various_values."time">='05:00' and various_values."time"<='05:30') then various_values.value end)/2 + date_st.value  as t5,
  sum(Case when (various_values."time">='06:00' and various_values."time"<='06:30') then various_values.value end)/2 + date_st.value  as t6,
  sum(Case when (various_values."time">='07:00' and various_values."time"<='07:30') then various_values.value end)/2 + date_st.value  as t7,
  sum(Case when (various_values."time">='08:00' and various_values."time"<='08:30') then various_values.value end)/2 + date_st.value  as t8,
  sum(Case when (various_values."time">='09:00' and various_values."time"<='09:30') then various_values.value end)/2 + date_st.value  as t9,
  sum(Case when (various_values."time">='10:00' and various_values."time"<='10:30') then various_values.value end)/2 + date_st.value  as t10,
  sum(Case when (various_values."time">='11:00' and various_values."time"<='11:30') then various_values.value end)/2 + date_st.value  as t11,
  sum(Case when (various_values."time">='12:00' and various_values."time"<='12:30') then various_values.value end)/2 + date_st.value  as t12,
    sum(Case when (various_values."time">='13:00' and various_values."time"<='13:30') then various_values.value end)/2 + date_st.value  as t13,
  sum(Case when (various_values."time">='14:00' and various_values."time"<='14:30') then various_values.value end)/2 + date_st.value  as t14,
  sum(Case when (various_values."time">='15:00' and various_values."time"<='15:30') then various_values.value end)/2 + date_st.value  as t15,
  sum(Case when (various_values."time">='16:00' and various_values."time"<='16:30') then various_values.value end)/2 + date_st.value  as t16,
  sum(Case when (various_values."time">='17:00' and various_values."time"<='17:30') then various_values.value end)/2 + date_st.value  as t17,
  sum(Case when (various_values."time">='18:00' and various_values."time"<='18:30') then various_values.value end)/2 + date_st.value  as t18,
  sum(Case when (various_values."time">='19:00' and various_values."time"<='19:30') then various_values.value end)/2 + date_st.value  as t19,
  sum(Case when (various_values."time">='20:00' and various_values."time"<='20:30') then various_values.value end)/2 + date_st.value  as t20,
  sum(Case when (various_values."time">='21:00' and various_values."time"<='21:30') then various_values.value end)/2 + date_st.value  as t21,
  sum(Case when (various_values."time">='22:00' and various_values."time"<='22:30') then various_values.value end)/2 + date_st.value  as t22,
  sum(Case when (various_values."time">='23:00' and various_values."time"<='23:30') then various_values.value end)/2 + date_st.value  as t23
FROM 
  public.abonents, 
  public.objects, 
  public.link_abonents_taken_params, 
  public.taken_params, 
  public.various_values, 
  public.params, 
  public.names_params,
  date_st
WHERE 
  abonents.guid_objects = objects.guid AND
  link_abonents_taken_params.guid_abonents = abonents.guid AND
  link_abonents_taken_params.guid_taken_params = taken_params.guid AND
  taken_params.guid_params = params.guid AND
  various_values.id_taken_params = taken_params.id AND
  params.guid_names_params = names_params.guid AND
  various_values.date = '19.12.2017' AND 
  names_params.name = 'R+ Профиль' and
  abonents.name='ГРЩ 1 Ввод2'

  group by   objects.name, 
  abonents.name,   
  names_params.name,
  date_st.value,
  coefficient, coefficient_2,        coefficient_3

