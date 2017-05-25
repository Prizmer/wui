# coding -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django import forms
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from openpyxl import Workbook
from openpyxl import load_workbook
import os
from django.db import connection
#from general.models import Objects, Abonents, TypesAbonents, Meters, MonthlyValues, DailyValues, CurrentValues, VariousValues, TypesParams, Params, TakenParams, LinkAbonentsTakenParams, Resources, TypesMeters, Measurement, NamesParams, BalanceGroups, LinkMetersComportSettings, LinkMetersTcpipSettings, ComportSettings, TcpipSettings, LinkBalanceGroupsMeters, Groups80020, LinkGroups80020Meters
from general.models import  Objects, Abonents, TcpipSettings, TypesAbonents, Meters, TypesMeters,LinkAbonentsTakenParams,LinkMetersComportSettings, LinkMetersTcpipSettings, ComportSettings,  TakenParams
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.db.models import signals

cfg_excel_name=""
cfg_sheet_name=""

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Create your views here.

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=150)
    path  = forms.FileField()

def MakeSheet(request):
    args={}
    fileName=""
    sheets=""
    if request.is_ajax():
        if request.method == 'GET':
            request.session["choice_file"]    = fileName    = request.GET['choice_file']
            #print fileName
            directory=os.path.join(BASE_DIR,'static/cfg/')
            wb=load_workbook(directory+fileName)
            sheets=wb.sheetnames

    args['sheets']=sheets
    return render_to_response("service/service_sheets_excel.html", args)

def choose_service(request):
    args={}
    directory=os.path.join(BASE_DIR,'static/cfg/')
    files = os.listdir(directory) 
    
    args['filesFF']= files
    return render_to_response("choose_service.html", args)

@csrf_exempt
def service_electric(request):
    args={}
    return render_to_response("service/service_electric.html", args)


def service_file(request):
    args={}
    args.update(csrf(request))    
    data_table=[]
    status='file not loaded'
    args['data_table'] = data_table
    args['status']=status

    return render_to_response("service/service_file.html", args)
    
def service_file_loading(request):
    args={}
    data_table=[]
    status='file not loaded'
    sPath=""
    if request.method == 'POST':        
        form = UploadFileForm(request.POST, request.FILES)
        #print form.as_table()
        #print form.is_valid()
        
        #print sPath
        if form.is_valid():
            sPath=os.path.join(BASE_DIR,'static/cfg/'+request.FILES['path'].name)
            handle_uploaded_file(request.FILES['path'])
            status= u'Файл загружен'
    else:
        form = UploadFileForm()
        
    args['data_table'] = data_table
    args['status']=status
    args['sPath']=sPath
    #print status
    return render_to_response("choose_service.html", args)

    
def service_electric_load(request):
    args={}
    data_table=[]
    status='file not loaded'

    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_file(request.FILES['path'])
            status='file loaded'
    else:
        form = UploadFileForm()
        
    args['data_table'] = data_table
    args['status']=status
    return render_to_response("service/service_electric.html", args)
    #return render_to_response("service/service_electric_load.html", args)
    
def handle_uploaded_file(f):

    destination = open(os.path.join(BASE_DIR,'static/cfg/'+f.name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    #print 'file load'
    destination.close()
    
def load_port(request):
    args={}
    #print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    fileName=""
    sheet    = ""
    tcp_ip_status    = ""
    object_status    = ""
    counter_status    = ""
    result=""
    if request.is_ajax():
        if request.method == 'GET':
            request.session["choice_file"]    = fileName    = request.GET['choice_file']
            request.session["choice_sheet"]    = sheet    = request.GET['choice_sheet']
            request.session["tcp_ip_status"]    = tcp_ip_status    = request.GET['tcp_ip_status']
            request.session["object_status"]    = object_status    = request.GET['object_status']
            request.session["counter_status"]    = counter_status    = request.GET['counter_status']
            
            #print fileName
            directory=os.path.join(BASE_DIR,'static/cfg/')
            sPath=directory+fileName
            #print sPath, sheet
            result=load_tcp_ip_or_com_ports_from_excel(sPath, sheet)
    print result
    if result:
        tcp_ip_status=u"Порт/ы был успешно добавлен"
    else:
        tcp_ip_status=u"Порт не был загружен, он уже существует в БД"
    
    
    #print fileName
    args["choice_file"]    = fileName
    args["choice_sheet"]    = sheet
    args["tcp_ip_status"]=tcp_ip_status
    args["object_status"]=object_status
    args["counter_status"]=counter_status
    return render_to_response("service/service_electric.html", args)

def checkPortIsExist(ip_adr,ip_port):
    dt_ports=[]
    cursor = connection.cursor()
    sQuery="""
    SELECT guid, ip_address, ip_port, write_timeout, read_timeout, attempts, 
       delay_between_sending
  FROM tcpip_settings
  where ip_address='%s' and  ip_port='%s'"""%(str(ip_adr).rstrip(),str(ip_port).rstrip())
    #print sQuery
    cursor.execute(sQuery)
    dt_ports = cursor.fetchall()
    #print dt_ports
    if len(dt_ports):  
        return False
    else: 
        return True

def load_tcp_ip_or_com_ports_from_excel(sPath, sSheet):
    #Добавление tcp_ip портов
    global cfg_excel_name
    cfg_excel_name=sPath
    global cfg_sheet_name
    cfg_sheet_name=sSheet
    wb = load_workbook(filename = sPath)
    sheet_ranges = wb[sSheet]
    row = 2
    result=""
    IsAdded=False
    portType=sheet_ranges[u'M1'].value
    while (bool(sheet_ranges[u'G%s'%(row)].value)):
        if sheet_ranges[u'G%s'%(row)].value is not None:
            print u'Обрабатываем строку ' + str(u'G%s '%(row)) + str(sheet_ranges[u'G%s'%(row)].value)
            ip_adr=sheet_ranges[u'K%s'%(row)].value
            ip_port=sheet_ranges[u'L%s'%(row)].value
            com_port=sheet_ranges[u'M%s'%(row)].value
            if portType==u'Com-port': #добавление com-порта
                print com_port
                if not com_port or com_port==None: 
                    result+="Отсутствует значение для com-порта в строке"+str(row)+". Заполните все ячейки excel таблицы."
                    break
                if not (SimpleCheckIfExist('comport_settings','name', com_port, "", "", "")):
                    add_port=ComportSettings(name=str(com_port).rstrip(),baudrate=9600,data_bits=8,parity=0,stop_bits=1, write_timeout=100, read_timeout=100, attempts=2, delay_between_sending=100)
                    add_port.save()
                    result+=u"Новый com-порт добавлен"
                    IsAdded=True
                else: result= u'Порт '+str(com_port)+u" уже существует"
            else:
                # проверка есть ли уже такой порт, запрос в БД с адресом и портом, если ответ пустой-добавляем, в противном случае continue
                if not ip_adr or not ip_port or ip_adr==None or ip_port==None: 
                    result+="Отсутствует значение/я для tcp/ip-порта в строке"+str(row)+". Заполните все ячейки excel таблицы."
                    break
                else:
                    if (checkPortIsExist(ip_adr,ip_port)):
                        add_port=TcpipSettings(ip_address = str(ip_adr).rstrip(), ip_port =int(ip_port), write_timeout =300 , read_timeout =700 , attempts =3 , delay_between_sending =400)
                        add_port.save()
                        result =u'Новый tcp/ip порт добавлен'
                        IsAdded=True
    #                add_meter = Meters(name = unicode(sheet_ranges[u'F%s'%(row)].value) + u' ' + unicode(sheet_ranges[u'E%s'%(row)].value), address = unicode(sheet_ranges[u'E%s'%(row)].value),  factory_number_manual = unicode(sheet_ranges[u'E%s'%(row)].value), guid_types_meters = TypesMeters.objects.get(guid = u"7cd88751-d232-410c-a0ef-6354a79112f1") )
    #                add_meter.save()
                    else: result+= u'Порт '+str(ip_adr)+": "+str(ip_port)+u" уже существует"
        print result
        row+=1
    return IsAdded

def SimpleCheckIfExist(table1,fieldName1, value1, table2, fieldName2, value2):
    dt=[]
    cursor = connection.cursor()
    if len(table2)==0: #проверка для двух сводных таблиц
        sQuery="""
        Select *
        from %s
        where %s.%s='%s'"""%(table1, table1, fieldName1, value1)
    else:#проверка для одной таблицы
        sQuery="""
        Select *
        from %s, %s
        where %s.guid_%s=%s.guid and
        %s.%s='%s' and
        %s.%s='%s'
        """%(table1,table2, table2, table1,table1, table1, fieldName1, value1,table2, fieldName2, value2)
    #print sQuery
    #print bool(dt)
    cursor.execute(sQuery)
    dt = cursor.fetchall()

    if not dt:  
        return False
    else: 
        return True
    
def GetSimpleTable(table,fieldName,value):
    dt=[]
    cursor = connection.cursor()
    sQuery="""
        Select *
        from %s
        where %s.%s='%s'"""%(table, table, fieldName, value)
    #print sQuery
    cursor.execute(sQuery)
    dt = cursor.fetchall()
    return dt
    

def GetTableFromExcel(sPath,sSheet):
    wb = load_workbook(filename = sPath)
    ws = wb[sSheet]
    row = 1
    dt=[]
    while (bool(ws[u'A%s'%(row)].value)):
        A=ws[u'A%s'%(row)].value
        B=ws[u'b%s'%(row)].value
        C=ws[u'c%s'%(row)].value
        D=ws[u'd%s'%(row)].value
        E=ws[u'e%s'%(row)].value
        F=ws[u'f%s'%(row)].value
        G=ws[u'g%s'%(row)].value
        H=ws[u'h%s'%(row)].value
        I=ws[u'i%s'%(row)].value
        J=ws[u'j%s'%(row)].value
        K=ws[u'k%s'%(row)].value
        L=ws[u'l%s'%(row)].value
        M=ws[u'm%s'%(row)].value
        
        vals =[A,B,C,D,E,F,G,H,I,J,K,L,M]
        dt.append(vals)
        row+=1
    return dt
    
def LoadObjectsAndAbons(sPath, sSheet):
    #Добавление объектов
    global cfg_excel_name
    cfg_excel_name=sPath
    global cfg_sheet_name
    cfg_sheet_name=sSheet
    result="Объекты не загружены"
    dtAll=GetTableFromExcel(sPath,sSheet) #получили из excel все строки до первой пустой строки (проверка по колонке А)
    
    for i in range(1,len(dtAll)):
        print u'Обрабатываем строку ' + dtAll[i][2]+' - '+dtAll[i][3]
        obj_l0=dtAll[i][0]
        obj_l1=dtAll[i][1]
        obj_l2=dtAll[i][2]
        abon=dtAll[i][3]
        account_1=dtAll[i][4]
        account_2=dtAll[i][5]
        isNewObj_l0=SimpleCheckIfExist('objects','name',obj_l0,"","","")
        isNewObj_l1=SimpleCheckIfExist('objects','name',obj_l1,"","","")
        isNewObj_l2=SimpleCheckIfExist('objects','name',obj_l2,"","","")
        isNewAbon=SimpleCheckIfExist('objects','name', obj_l2,'abonents', 'name', abon)
        kv=0
        if not (isNewObj_l0):
            print 'create object '+obj_l0
            add_parent_object = Objects( name=obj_l0, level=0)
            add_parent_object.save()
            print 'create object '+obj_l1
            #print add_parent_object
            add_object1=Objects(name=obj_l1, level=1, guid_parent = add_parent_object)
            add_object1.save()
            print 'create object '+obj_l2
            add_object2=Objects(name=obj_l2, level=2, guid_parent = add_object1)
            add_object2.save()
            
            print 'create abonent '+abon
            add_abonent = Abonents(name = abon, account_1 =unicode(account_1), account_2 =unicode(account_2), guid_objects =add_object2, guid_types_abonents = TypesAbonents.objects.get(guid= u"e4d813ca-e264-4579-ae15-385cdbf5d28c"))
            add_abonent.save()
            result=u"Объекты: "+obj_l0+", "+obj_l1+u", "+obj_l2+u","+abon+u" созданы"
            continue
        if not (isNewObj_l1):
            print 'create object '+obj_l1
            dtParent=GetSimpleTable('objects','name',obj_l0)
            if dtParent: #родительский объект есть
                guid_parent=dtParent[0][0]
                add_object1=Objects(name=obj_l1, level=1, guid_parent = Objects.objects.get(guid=guid_parent))
                add_object1.save()                
                add_object2=Objects(name=obj_l2, level=2, guid_parent = add_object1)
                add_object2.save()
                print 'create abonent '+abon
                add_abonent = Abonents(name = abon, account_1 =unicode(account_1), account_2 =unicode(account_2), guid_objects =add_object2, guid_types_abonents = TypesAbonents.objects.get(guid= u"e4d813ca-e264-4579-ae15-385cdbf5d28c"))
                add_abonent.save()
                result+=u"Объекты: "+obj_l1+u", "+obj_l2+u","+abon+u" созданы"
                continue
        if not (isNewObj_l2):
            print 'create object '+obj_l2
            dtParent=GetSimpleTable('objects','name',obj_l1)
            if dtParent: #родительский объект есть
                guid_parent=dtParent[0][0]                
                add_object = Objects(name=obj_l2, level=2, guid_parent = Objects.objects.get(guid=guid_parent))
                add_object.save()
                result+=u"Объект: "+obj_l2+u" создан"
        if not (isNewAbon):
            print 'create abonent '+ abon
            dtObj=GetSimpleTable('objects','name',obj_l2)
            if dtObj: #родительский объект есть
                guid_object=dtObj[0][0]
                add_abonent = Abonents(name = abon, account_1 =unicode(account_1), account_2 =unicode(account_2), guid_objects = Objects.objects.get(guid=guid_object), guid_types_abonents = TypesAbonents.objects.get(guid= u"e4d813ca-e264-4579-ae15-385cdbf5d28c"))
                add_abonent.save()
                kv+=1

    result+=u" Прогружено "+str(kv)+u" абонентов"

    return result

def load_electric_objects(request):
    args={}
    fileName=""
    sheet    = ""
    tcp_ip_status    = ""
    object_status    = ""
    counter_status    = ""
    result="Не загружено"
    if request.is_ajax():
        if request.method == 'GET':
            request.session["choice_file"]    = fileName    = request.GET['choice_file']
            request.session["choice_sheet"]    = sheet    = request.GET['choice_sheet']
            request.session["tcp_ip_status"]    = tcp_ip_status    = request.GET['tcp_ip_status']
            request.session["object_status"]    = object_status    = request.GET['object_status']
            request.session["counter_status"]    = counter_status    = request.GET['counter_status']
            
            directory=os.path.join(BASE_DIR,'static/cfg/')
            sPath=directory+fileName
            result=LoadObjectsAndAbons(sPath, sheet)
    
    object_status=result#"Загрузка объектов условно прошла"

    #print fileName
    args["choice_file"]    = fileName
    args["choice_sheet"]    = sheet
    args["tcp_ip_status"]=tcp_ip_status
    args["object_status"]=object_status
    args["counter_status"]=counter_status
    return render_to_response("service/service_electric.html", args)
    
def LoadElectricMeters(sPath, sSheet):
    global cfg_excel_name
    cfg_excel_name=sPath
    global cfg_sheet_name
    cfg_sheet_name=sSheet
    result=u"Счётчики не загружены"
    dtAll=GetTableFromExcel(sPath,sSheet) #получили из excel все строки до первой пустой строки (проверка по колонке А)
    met=0
    for i in range(1,len(dtAll)):
        print u'Обрабатываем строку ' + dtAll[i][3]+' - '+dtAll[i][6]
        obj_l2=dtAll[i][2] #корпус
        abon=dtAll[i][3] #квартира
        meter=dtAll[i][6] #номер счётчика
        adr=dtAll[i][7] #номер в сети
        type_meter=dtAll[i][8] #тип счётчика
        NumLic=dtAll[i][5] #номер лицевого счёта, тут используется как пароль для м-230-ум
        Group=dtAll[i][12]
        isNewMeter=SimpleCheckIfExist('meters','factory_number_manual',meter,"","","")
        isNewAbon=SimpleCheckIfExist('objects','name', obj_l2,'abonents', 'name', abon)        
        
        print u'счётчик существует ', isNewMeter
        if not (isNewAbon):
            return u"Сначала создайте стурктуру объектов и абонентов"
        if not (isNewMeter):
            
            print 'create meter '+meter +" adress: "+adr
            if unicode(type_meter) == u'М-200':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), guid_types_meters = TypesMeters.objects.get(guid = u"6224d20b-1781-4c39-8799-b1446b60774d") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'М-200'
                
                
            elif unicode(type_meter) == u'М-230':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), password = 111111 , factory_number_manual = unicode(meter), guid_types_meters = TypesMeters.objects.get(guid = u"423b33a7-2d68-47b6-b4f6-5b470aedc4f4") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'М-230'
                
            elif unicode(type_meter) == u'М-230-УМ':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), password = unicode(NumLic) , factory_number_manual = unicode(meter), guid_types_meters = TypesMeters.objects.get(guid = u"20e4767a-49e5-4f84-890c-25e311339c28") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'М-230-УМ'
                
            elif unicode(type_meter) == u'Эльф 1.08':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), guid_types_meters = TypesMeters.objects.get(guid = u"1c5a8a80-1c51-4733-8332-4ed8d510a650") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'Эльф 1.08'
            elif unicode(type_meter) == u'СПГ762-1':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), guid_types_meters = TypesMeters.objects.get(guid = u"c3ec5c22-d184-41c5-b6bf-66fa30215a41") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'СПГ762-1'
                
            elif unicode(type_meter) == u'СПГ762-2':
                add_meter = Meters(name=unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), guid_types_meters = TypesMeters.objects.get(guid = u"5eb7dd59-faf9-4ead-8654-4f3de74de2b0") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'СПГ762-2'
            elif unicode(type_meter) == u'СПГ762-3':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), guid_types_meters = TypesMeters.objects.get(guid = u"e4fb7950-a44f-41f0-a6ff-af5e30d9d562") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'СПГ762-3'
            elif unicode(type_meter) == u'Sayany':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), guid_types_meters = TypesMeters.objects.get(guid = u"5429b439-233e-4944-b91b-4b521a10f77b") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'Sayany'
            elif unicode(type_meter) == u'Tekon_hvs':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), password = unicode(Group), guid_types_meters = TypesMeters.objects.get(guid = u"8398e7d6-39f7-45d2-9c45-a1c48e751b61") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'Tekon_gvs'
            elif unicode(type_meter) == u'Tekon_hvs':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), password = unicode(Group), guid_types_meters = TypesMeters.objects.get(guid = u"64f02a2c-41e1-48b2-bc72-7873ea9b6431") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'Tekon_gvs'

            elif unicode(type_meter) == u'Tekon_heat':
                add_meter = Meters(name = unicode(type_meter) + u' ' + unicode(meter), address = unicode(adr), factory_number_manual = unicode(meter), password = unicode(Group), guid_types_meters = TypesMeters.objects.get(guid = u"b53173f2-2307-4b70-b84c-61b634521e87") )
                add_meter.save()
                print u'Прибор добавлен' + ' --->   ' + u'Tekon_heat'
            else:
                print u'Не найдено совпадение с существующим типом прибора'
                met-=1
            met+=1
            
    result=u" Загружено счётчиков "+str(met)
    
    return result


def load_electric_counters(request):
    args={}
    if request.is_ajax():
        if request.method == 'GET':
            request.session["choice_file"]    = fileName    = request.GET['choice_file']
            request.session["choice_sheet"]    = sheet    = request.GET['choice_sheet']
            request.session["tcp_ip_status"]    = tcp_ip_status    = request.GET['tcp_ip_status']
            request.session["object_status"]    = object_status    = request.GET['object_status']
            request.session["counter_status"]    = counter_status    = request.GET['counter_status']
            directory=os.path.join(BASE_DIR,'static/cfg/')
            sPath=directory+fileName
            result=LoadElectricMeters(sPath, sheet)
    counter_status=result#"Загрузка счётчиков условно прошла"
        
    #print fileName
    args["choice_file"]    = fileName
    args["choice_sheet"]    = sheet
    args["tcp_ip_status"]=tcp_ip_status
    args["object_status"]=object_status
    args["counter_status"]=counter_status
    return render_to_response("service/service_electric.html", args)


@csrf_exempt
def service_water(request):
    args={}
    return render_to_response("service/service_water.html", args)
    
def add_link_meter_port_from_excel_cfg_electric(sender, instance, created, **kwargs):
    """Делаем привязку счётчика к порту по excel файлу ведомости"""    
    dtAll=GetTableFromExcel(cfg_excel_name,cfg_sheet_name) #получили из excel все строки до первой пустой строки (проверка по колонке А)
    
    for i in range(1,len(dtAll)):
        print u'Обрабатываем строку ' + dtAll[i][6]+' - '+dtAll[i][7]
        meter=dtAll[i][6] #счётчик
        PortType=dtAll[0][12] # com или tcp-ip
        #print 'i=',i,' len=', len(dtAll)
        ip_adr=unicode(dtAll[i][10]).strip()
        ip_port=unicode(dtAll[i][11]).strip()
        # Привязка к tpc порту
        if meter is not None:
            if unicode(meter) == instance.factory_number_manual :
                if unicode(PortType) == u'Com-port':
                    guid_com_port_from_excel = connection.cursor()
                    guid_com_port_from_excel.execute("""SELECT 
                                                      comport_settings.guid
                                                    FROM 
                                                      public.comport_settings
                                                    WHERE 
                                                      comport_settings.name = '%s';"""%(unicode(dtAll[i][12])))
                    guid_com_port_from_excel = guid_com_port_from_excel.fetchall()
            
                    guid_com_port = ComportSettings.objects.get(guid=guid_com_port_from_excel[0][0])
                    add_com_port_link = LinkMetersComportSettings(guid_meters = instance, guid_comport_settings = guid_com_port)
                    add_com_port_link.save()
                
                else:
                    guid_ip_port_from_excel = connection.cursor()
                    sQuery="""SELECT tcpip_settings.guid
                                                    FROM 
                                                      public.tcpip_settings
                                                    WHERE 
                                                      tcpip_settings.ip_address = '%s' AND 
                                                      tcpip_settings.ip_port = '%s';"""%(ip_adr, ip_port)
                    #print sQuery
                    guid_ip_port_from_excel.execute(sQuery)
                    guid_ip_port_from_excel = guid_ip_port_from_excel.fetchall()
            
                    print guid_ip_port_from_excel
                    guid_ip_port = TcpipSettings.objects.get(guid=guid_ip_port_from_excel[0][0])
                    add_ip_port_link = LinkMetersTcpipSettings(guid_meters = instance, guid_tcpip_settings = guid_ip_port)            
                    add_ip_port_link.save()
            else:
                pass
            
signals.post_save.connect(add_link_meter_port_from_excel_cfg_electric, sender=Meters)
            
def add_link_abonent_taken_params_from_excel_cfg_electric(sender, instance, created, **kwargs):
    dtAll=GetTableFromExcel(cfg_excel_name,cfg_sheet_name) #получили из excel все строки до первой пустой строки (проверка по колонке А)
    #print dtAll[0][0]
    for i in range(1,len(dtAll)):
        meter=dtAll[i][6]
        abon=unicode(dtAll[i][3])
        obj=unicode(dtAll[i][2])
        if meter is not None:
            cursor = connection.cursor()
            sQuery="""SELECT abonents.guid FROM public.objects, public.abonents
                      WHERE objects.guid = abonents.guid_objects 
                      AND abonents.name = '%s' 
                      AND objects.name = '%s';"""%(abon,obj )
            #print sQuery
            cursor.execute(sQuery)
            guid_abonent_by_excel = cursor.fetchall()
            #print guid_abonent_by_excel

            if unicode(meter) == instance.guid_meters.factory_number_manual:
                print u'Абонент найден' + u' ' + unicode(instance.name)
                #print guid_abonent_by_excel 
                add_link_abonents_taken_param = LinkAbonentsTakenParams (name = unicode(dtAll[i][3]) + u' - ' +  unicode(instance.guid_meters.name)  ,coefficient=unicode(dtAll[i][9]), coefficient_2 = 1, guid_abonents = Abonents.objects.get(guid =guid_abonent_by_excel[0][0]), guid_taken_params = instance)
                add_link_abonents_taken_param.save()
            else:
                pass
    
signals.post_save.connect(add_link_abonent_taken_params_from_excel_cfg_electric, sender=TakenParams)

def load_water_objects(request):
    args={}
    fileName=""
    sheet    = ""
    tcp_ip_status    = ""
    object_status    = ""
    counter_status    = ""
    result="Не загружено"
    if request.is_ajax():
        if request.method == 'GET':
            request.session["choice_file"]    = fileName    = request.GET['choice_file']
            request.session["choice_sheet"]    = sheet    = request.GET['choice_sheet']
            request.session["tcp_ip_status"]    = tcp_ip_status    = request.GET['tcp_ip_status']
            request.session["object_status"]    = object_status    = request.GET['object_status']
            request.session["counter_status"]    = counter_status    = request.GET['counter_status']
            
            directory=os.path.join(BASE_DIR,'static/cfg/')
            sPath=directory+fileName
            result=LoadObjectsAndAbons_water(sPath, sheet)
    
    object_status=result

    #print fileName
    args["choice_file"]    = fileName
    args["choice_sheet"]    = sheet
    args["port_status"]=tcp_ip_status
    args["object_status"]=object_status
    args["counter_status"]=counter_status
    return render_to_response("service/service_water.html", args)
    
def LoadObjectsAndAbons_water(sPath, sheet):
    result=""
    dtAll=GetTableFromExcel(sPath,sheet) #получили из excel все строки до первой пустой строки (проверка по колонке А)
    kv=0
    for i in range(2,len(dtAll)):
        print u'Обрабатываем строку ' + dtAll[i][2]+' - '+dtAll[i][3]
        obj_l0=u'Вода' # всегда будет Вода как объект-родитель
        obj_l1=dtAll[i][0] #корпус
        obj_l2=dtAll[i][1] #квартира
        if not dtAll[i][1] or dtAll[i][1]==None:
            j=i
            while not obj_l2 or obj_l2==None:
                j-=1
                obj_l2=dtAll[j][1]
        print obj_l2
        abon=dtAll[i][2] #абонент он же счётчик  воде
#        chanel=dtAll[i][4] # канал пульсара
#        numPulsar=dtAll[i][5] #номер пульсара
#        typePulsar=dtAll[i][5] #тип пульсара
        isNewObj_l0=SimpleCheckIfExist('objects','name',obj_l0,"","","")
        isNewObj_l1=SimpleCheckIfExist('objects','name',obj_l1,"","","")
        isNewObj_l2=SimpleCheckIfExist('objects','name',obj_l2,"","","")
        isNewAbon=SimpleCheckIfExist('objects','name', obj_l2,'abonents', 'name', abon)
        
        if not (isNewObj_l0):
            print 'create object '+obj_l0
            add_parent_object = Objects(name=obj_l0, level=0) 
            add_parent_object.save()
            print 'create object '+obj_l1
            #print add_parent_object
            add_object1=Objects(name=obj_l1, level=1, guid_parent = add_parent_object)
            add_object1.save()
            print 'create object '+obj_l2
            add_object2=Objects(name=obj_l2, level=2, guid_parent = add_object1)
            add_object2.save()
            
            print 'create abonent '+abon
            add_abonent = Abonents(name = abon, guid_objects =add_object2, guid_types_abonents = TypesAbonents.objects.get(guid= u"e4d813ca-e264-4579-ae15-385cdbf5d28c"))
            add_abonent.save()
            kv+=1
            result=u"Объекты: "+obj_l0+", "+obj_l1+u", "+obj_l2+u","+abon+u" созданы"
            continue
        if not (isNewObj_l1):
            print 'create object '+obj_l1
            dtParent=GetSimpleTable('objects','name',obj_l0)
            if dtParent: #родительский объект есть
                guid_parent=dtParent[0][0]
                add_object1=Objects(name=obj_l1, level=1, guid_parent = Objects.objects.get(guid=guid_parent))
                add_object1.save()                
                add_object2=Objects(name=obj_l2, level=2, guid_parent = add_object1)
                add_object2.save()
                print 'create abonent '+abon
                add_abonent = Abonents(name = abon, guid_objects =add_object2, guid_types_abonents = TypesAbonents.objects.get(guid= u"e4d813ca-e264-4579-ae15-385cdbf5d28c"))
                add_abonent.save()
                kv+=1
                result+=u"Объекты: "+obj_l1+u", "+obj_l2+u","+abon+u" созданы"
                continue
        if not (isNewObj_l2):
            print 'create object '+obj_l2
            dtParent=GetSimpleTable('objects','name',obj_l1)
            if dtParent: #родительский объект есть
                guid_parent=dtParent[0][0]                
                add_object = Objects(name=obj_l2, level=2, guid_parent = Objects.objects.get(guid=guid_parent))
                add_object.save()
                result+=u"Объект: "+obj_l2+u" создан"
        if not (isNewAbon):
            print 'create abonent '+ abon
            dtObj=GetSimpleTable('objects','name',obj_l2)
            if dtObj: #родительский объект есть
                guid_object=dtObj[0][0]
                add_abonent = Abonents(name = abon, guid_objects = Objects.objects.get(guid=guid_object), guid_types_abonents = TypesAbonents.objects.get(guid= u"e4d813ca-e264-4579-ae15-385cdbf5d28c"))
                add_abonent.save()
                kv+=1

    result+=u" Прогружено "+str(kv)+u" водо-счётчиков"

    return result