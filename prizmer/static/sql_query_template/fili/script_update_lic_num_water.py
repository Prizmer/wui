# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:53:01 2017

@author: Елена
"""

import psycopg2


def get_sQuery_korp(num):
    sQuery="""With Korp as 
    (SELECT 
  objects.name, 
  objects.guid_parent, 
  objects.guid
FROM 
  public.objects
WHERE 
  objects.name LIKE '%%Корпус%%%s%%Вода%%'
  )
SELECT 
  Korp.name,
  abonents.guid, 
  abonents.name, 
  abonents.account_1, 
  abonents.account_2, 
  objects.name
FROM 
  Korp,
  public.abonents, 
  public.objects
WHERE 
  objects.guid_parent=Korp.guid and
  abonents.guid_objects = objects.guid """ %(str(num))
    return sQuery
    
def get_sQuery_heat_electric_by_korp(num):
    sQuery="""
    SELECT 
  objects.guid, 
  objects.name, 
  abonents.guid, 
  abonents.name, 
  abonents.account_2
FROM 
  public.abonents, 
  public.objects
WHERE 
  abonents.guid_objects = objects.guid and
  account_2 = 'None'
  and  
  objects.name like '%%Корпус%%%s%%'
    """%(num)
    
    return sQuery
    
# Для воды
connection = psycopg2.connect(host='localhost',
                             port=5432,
                             dbname='prizmer',
                             user='postgres',
                             password='1')
cursor=connection.cursor()

for k in range(1,4):
    cursor.execute(get_sQuery_korp(k))
    data_table = cursor.fetchall()
    koef=5501000
    if (k==2): 
        koef=5502000
    elif (k==3): 
        koef=5503000
    for i in range(len(data_table)):
        data_table[i]=list(data_table[i])
        sLic_num=str(data_table[i][5])[16:]
        #print sLic_num
        lic_num=int(sLic_num)+koef
        #print  lic_num
        sQuery_update="""UPDATE abonents
        SET  account_2='%s'
        WHERE guid='%s'"""%(str(lic_num),str(data_table[i][1]))
        cursor.execute(sQuery_update)
    print 'Done '+str(k)

# Для тепла и воды

for k in range(1,4):
    cursor.execute(get_sQuery_heat_electric_by_korp(k))
    data_table = cursor.fetchall()
    koef=5501000
    if (k==2): 
        koef=5502000
    elif (k==3): 
        koef=5503000
    for i in range(len(data_table)):
        data_table[i]=list(data_table[i])
        sLic_num=str(data_table[i][3])[16:]
        #print sLic_num
        lic_num=int(sLic_num)+koef
        #print  lic_num
        sQuery_update="""UPDATE abonents
        SET  account_2='%s'
        WHERE guid='%s'"""%(str(lic_num),str(data_table[i][2]))
        cursor.execute(sQuery_update)
    print 'Done '+str(k)

connection.commit()
cursor.close()
