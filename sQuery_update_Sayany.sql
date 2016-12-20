Update public.meters
set name='Sayany' || substring(name from 13 for bit_length(name))
where meters.name like 'Саяны %'


