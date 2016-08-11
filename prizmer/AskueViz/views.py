# coding -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
import simplejson as json
from django.db import connection
import datetime

from AskueViz.models import DiagramMainframe
# Create your views here.

A_plus_tag = 'кВт*ч'
R_plus_tag = 'кВар*ч'
P_tag = 'кВт'
Q_tag = 'кВАр'
U_tag = 'В'
I_tag = 'А'

def daily_value(adress): # Извлечение значение на начало текущих суток
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
  daily_values.value
FROM 
  public.daily_values, 
  public.taken_params, 
  public.meters
WHERE 
  daily_values.id_taken_params = taken_params.id AND
  taken_params.guid_meters = meters.guid AND
  meters.address = %s AND 
  daily_values.date = %s LIMIT 1;""",[adress, datetime.datetime.now().date()])
    simpleq = simpleq.fetchall()
    return simpleq
    
def serial_number_by_address(adress): # Извлечение заводского номера по сетевому адрему
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                         meters.factory_number_manual
                       FROM 
                         public.meters
                       WHERE 
                         meters.address = %s LIMIT 1;""",[adress])
    simpleq = simpleq.fetchall()
    return simpleq
    
def name_by_address(adress): # Извлечение имени по сетевому адрему
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                         meters.name
                       FROM 
                         public.meters
                       WHERE 
                         meters.address = %s LIMIT 1;""",[adress])
    simpleq = simpleq.fetchall()
    return simpleq
    
def cofficient_by_address(adress): # Извлечение Ктн по сетевому адрему
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          link_abonents_taken_params.coefficient
                        FROM 
                          public.link_abonents_taken_params, 
                          public.meters, 
                          public.taken_params
                        WHERE 
                          taken_params.guid_meters = meters.guid AND
                          taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                          meters.address = %s 
                        LIMIT 1;""",[adress])
    simpleq = simpleq.fetchall()
    return simpleq[0][0]
    
def cofficient_2_by_address(adress): # Извлечение Ктт по сетевому адрему
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          link_abonents_taken_params.coefficient_2
                        FROM 
                          public.link_abonents_taken_params, 
                          public.meters, 
                          public.taken_params
                        WHERE 
                          taken_params.guid_meters = meters.guid AND
                          taken_params.guid = link_abonents_taken_params.guid_taken_params AND
                          meters.address = %s 
                        LIMIT 1;""",[adress])
    simpleq = simpleq.fetchall()
    return simpleq[0][0]
	
def current_value(adress, param_name): # Извлечение значения текущего
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          current_values.value
                       FROM 
                          public.current_values, 
                          public.meters, 
                          public.taken_params, 
                          public.params, 
                          public.names_params
                       WHERE 
                          taken_params.guid_meters = meters.guid AND
                          taken_params.id = current_values.id_taken_params AND
                          taken_params.guid_params = params.guid AND
                          params.guid_names_params = names_params.guid AND
                          meters.address = %s AND 
                          names_params.name = %s LIMIT 1 ;""",[adress, param_name])
    simpleq = simpleq.fetchall()
    try:
        return simpleq[0][0]
    except:
        return simpleq
        
def current_value_ktn_ktt(adress, param_name): # Извлечение значения текущего с учетом коэффициента трансформации тока и напряжения
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          current_values.value
                       FROM 
                          public.current_values, 
                          public.meters, 
                          public.taken_params, 
                          public.params, 
                          public.names_params
                       WHERE 
                          taken_params.guid_meters = meters.guid AND
                          taken_params.id = current_values.id_taken_params AND
                          taken_params.guid_params = params.guid AND
                          params.guid_names_params = names_params.guid AND
                          meters.address = %s AND 
                          names_params.name = %s LIMIT 1 ;""",[adress, param_name])
    simpleq = simpleq.fetchall()
    try:
        return int(simpleq[0][0]*cofficient_2_by_address(adress)*cofficient_by_address(adress))/1000
    except:
        return simpleq
        
def current_value_ktt(adress, param_name): # Извлечение значения текущего с учетом коэффициента трансформации тока
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          current_values.value
                       FROM 
                          public.current_values, 
                          public.meters, 
                          public.taken_params, 
                          public.params, 
                          public.names_params
                       WHERE 
                          taken_params.guid_meters = meters.guid AND
                          taken_params.id = current_values.id_taken_params AND
                          taken_params.guid_params = params.guid AND
                          params.guid_names_params = names_params.guid AND
                          meters.address = %s AND 
                          names_params.name = %s LIMIT 1 ;""",[adress, param_name])
    simpleq = simpleq.fetchall()
    try:
        return simpleq[0][0]*cofficient_2_by_address(adress)
    except:
        return simpleq
        
def current_value_ktn(adress, param_name): # Извлечение значения текущего с учетом коэффициента трансформации напряжения
    simpleq = connection.cursor()
    simpleq.execute("""SELECT 
                          current_values.value
                       FROM 
                          public.current_values, 
                          public.meters, 
                          public.taken_params, 
                          public.params, 
                          public.names_params
                       WHERE 
                          taken_params.guid_meters = meters.guid AND
                          taken_params.id = current_values.id_taken_params AND
                          taken_params.guid_params = params.guid AND
                          params.guid_names_params = names_params.guid AND
                          meters.address = %s AND 
                          names_params.name = %s LIMIT 1 ;""",[adress, param_name])
    simpleq = simpleq.fetchall()
    try:
        return simpleq[0][0]*cofficient_by_address(adress)
    except:
        return simpleq
    
def viz_values(start_left_point, start_top_point, adress_num):
    
    values = {}
    
    val1={}
    val1['caption'] = u'№ ', serial_number_by_address(adress_num)
    val1['value'] =   name_by_address(adress_num)
    val1['color'] = 'Blue'
    val1['showonmain'] = 1
    val1['mvalleft'] = start_left_point + 48
    val1['mvaltop'] = start_top_point
    
    val2={}
    val2['caption'] = u'Ктн = ', cofficient_by_address(adress_num)
    val2['value'] = u'Ктт = ', cofficient_2_by_address(adress_num)
    val2['color'] = 'Black'
    val2['showonmain'] = 0
	
    val3={}
    val3['caption'] = u'T0 A+'
    val3['value'] = current_value(adress_num, u'T0 A+'), A_plus_tag
    val3['color'] = 'Green'
    val3['showonmain'] = 1
    val3['mvalleft'] = start_left_point + 48
    val3['mvaltop'] = start_top_point + 10
    
    val4={}
    val4['caption'] = u'T0 R+'
    val4['value'] = current_value(adress_num, u'T0 R+'), R_plus_tag
    val4['color'] = 'Green'
    val4['showonmain'] = 0

    val5={}
    val5['caption'] = u'P'
    val5['value'] = current_value_ktn_ktt(adress_num, u'P'), P_tag
    val5['color'] = 'Green'
    val5['showonmain'] = 1
    val5['mvalleft'] = start_left_point + 48
    val5['mvaltop'] = start_top_point + 28
	
    val6={}
    val6['caption'] = u'Q'
    val6['value'] = current_value_ktn_ktt(adress_num, u'Q'), Q_tag
    val6['color'] = 'Green'
    val6['showonmain'] = 1
    val6['mvalleft'] = start_left_point + 48
    val6['mvaltop'] = start_top_point + 40

    val7={}
    val7['caption'] = u'Ia'
    val7['value'] = current_value_ktt(adress_num, u'Ia'), I_tag
    val7['color'] = 'Red'
    val7['showonmain'] = 0
	
    val8={}
    val8['caption'] = u'Ib'
    val8['value'] = current_value_ktt(adress_num, u'Ib'), I_tag
    val8['color'] = 'Red'
    val8['showonmain'] = 0

    val9={}
    val9['caption'] = u'Ic'
    val9['value'] = current_value_ktt(adress_num, u'Ic'), I_tag
    val9['color'] = 'Red'
    val9['showonmain'] = 0
	
    val10={}
    val10['caption'] = u'Ua'
    val10['value'] = current_value_ktn(adress_num, u'Ua'), U_tag
    val10['color'] = 'Green'
    val10['showonmain'] = 0
  
    val11={}
    val11['caption'] = u'Ub'
    val11['value'] = current_value_ktn(adress_num, u'Ub'), U_tag
    val11['color'] = 'Green'
    val11['showonmain'] = 0
	
    val12={}
    val12['caption'] = u'Uc'
    val12['value'] = current_value_ktn(adress_num, u'Uc'), U_tag
    val12['color'] = 'Green'
    val12['showonmain'] = 0


    values['1'] = val1 
    values['2'] = val2      
    values['3'] = val3
    values['4'] = val4
    values['5'] = val5    
    values['6'] = val6      
    values['7'] = val7
    values['8'] = val8
    values['9'] = val9
    values['10'] = val10
    values['11'] = val11
    values['12'] = val12
    return values


def viz_mainframe(request):
    
    mainframe = {}
    mainframe['refreshmentTimeMS'] = 3000
    mainframe['mainframeleft']= 10
    mainframe['mainframetop'] = 10
    mainframe['mainframewidth'] = 1700
    mainframe['mainframeheight'] = 1150
    mainframe['backgroundurl'] = u'ЭОМ.png'
    
    return JsonResponse(mainframe, safe=False)
    
def viz_devices(request):
    
    devices = {}
    
# Устройство Сетевой адрес 11
    start_left_point = 40 
    start_top_point = 10
    adress_num = 11	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device11'] = device
    
# Устройство Сетевой адрес 9
    start_left_point = 40 
    start_top_point = 76
    adress_num = 9	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device9'] = device
    
# Устройство Сетевой адрес 10
    start_left_point = 183 
    start_top_point = 76
    adress_num = 10	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device10'] = device
	
 # Устройство Сетевой адрес 8
    start_left_point = 382
    start_top_point = 76
    adress_num = 8	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device8'] = device

 # Устройство Сетевой адрес 7
    start_left_point = 526
    start_top_point = 76
    adress_num = 7	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device7'] = device
	
 # Устройство Сетевой адрес 6
    start_left_point = 382
    start_top_point = 10
    adress_num = 6	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device6'] = device
	
 # Устройство Сетевой адрес 12
    start_left_point = 40
    start_top_point = 282
    adress_num = 12	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device12'] = device

	
# Устройство Сетевой адрес 13
    start_left_point = 168
    start_top_point = 282
    adress_num = 13	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device13'] = device
	
# Устройство Сетевой адрес 14
    start_left_point = 308
    start_top_point = 282
    adress_num = 14	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device14'] = device
	
# Устройство Сетевой адрес 19
    start_left_point = 568
    start_top_point = 282
    adress_num = 19	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device19'] = device
	
# Устройство Сетевой адрес 15
    start_left_point = 310
    start_top_point = 350
    adress_num = 15	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device15'] = device
	
# Устройство Сетевой адрес 16
    start_left_point = 440
    start_top_point = 350
    adress_num = 16	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device16'] = device
	
# Устройство Сетевой адрес 18
    start_left_point = 568
    start_top_point = 350
    adress_num = 18	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device18'] = device
	
# Устройство Сетевой адрес 17
    start_left_point = 697
    start_top_point = 350
    adress_num = 17	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device17'] = device
	
# Устройство Сетевой адрес 25
    start_left_point = 846
    start_top_point = 350
    adress_num = 25	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device25'] = device
	
# Устройство Сетевой адрес 30
    start_left_point = 975
    start_top_point = 350
    adress_num = 30	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device30'] = device
	
# Устройство Сетевой адрес 32
    start_left_point = 1103
    start_top_point = 350
    adress_num = 32	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device32'] = device
	
# Устройство Сетевой адрес 26
    start_left_point = 1233
    start_top_point = 350
    adress_num = 26	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device26'] = device
	
# Устройство Сетевой адрес 20
    start_left_point = 116
    start_top_point = 470
    adress_num = 20	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device20'] = device
	
	# Устройство Сетевой адрес 55
    start_left_point = 432
    start_top_point = 470
    adress_num = 55	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device55'] = device
	
	# Устройство Сетевой адрес 1
    start_left_point = 4
    start_top_point = 593
    adress_num = 1	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device1'] = device
	
	# Устройство Сетевой адрес 2
    start_left_point = 133
    start_top_point = 593
    adress_num = 2	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device2'] = device
	
	# Устройство Сетевой адрес 3
    start_left_point = 262
    start_top_point = 593
    adress_num = 3	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device3'] = device
	
	# Устройство Сетевой адрес 35
    start_left_point = 432
    start_top_point = 593
    adress_num = 35	
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device35'] = device
	
	# Устройство Сетевой адрес 29
    start_left_point = 582
    start_top_point = 593
    adress_num = 29
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device29'] = device
	
	# Устройство Сетевой адрес 34
    start_left_point = 712
    start_top_point = 593
    adress_num = 34
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device34'] = device
	
	# Устройство Сетевой адрес 33
    start_left_point = 840
    start_top_point = 593
    adress_num = 33
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device33'] = device
	
	# Устройство Сетевой адрес 21
    start_left_point = 970
    start_top_point = 593
    adress_num = 21
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device21'] = device
	
	# Устройство Сетевой адрес 4
    start_left_point = 1234
    start_top_point = 593
    adress_num = 4
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device4'] = device
	
	# Устройство Сетевой адрес 5
    start_left_point = 1389
    start_top_point = 593
    adress_num = 5
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device5'] = device
	
	# Устройство Сетевой адрес 28
    start_left_point = 4
    start_top_point = 1042
    adress_num = 28
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device28'] = device
	
	# Устройство Сетевой адрес 23
    start_left_point = 133
    start_top_point = 1042
    adress_num = 23
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device23'] = device
	
	# Устройство Сетевой адрес 31
    start_left_point = 261
    start_top_point = 1042
    adress_num = 31
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device31'] = device
	
	# Устройство Сетевой адрес 24
    start_left_point = 391
    start_top_point = 1042
    adress_num = 24
    device = {}
    device['deviceboxleft']   = start_left_point
    device['deviceboxtop']    = start_top_point
    device['deviceboxwidth']  = 40
    device['deviceboxheight'] = 50

    device['values'] = viz_values(start_left_point, start_top_point, adress_num)
    devices['device24'] = device

    
    
    
    return JsonResponse(devices, safe=False)
    
    
def energo_scheme(request):
    args = {}
    return render_to_response("energo_schema.html", args)