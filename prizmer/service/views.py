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
import sys

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
#    return HttpResponse(sheets)
            
            
def choose_service(request):
    args={}
    #fileName=request.session['choice_file']
#    fileName=""
#    if request.is_ajax():
#        if request.method == 'GET':
#            request.session["choice_file"]    = fileName    = request.GET['choice_file']
#            print fileName
    
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
    
def load_tcp_ip(request):
    args={}
    if request.is_ajax():
        if request.method == 'GET':
            request.session["choice_file"]    = fileName    = request.GET['choice_file']
            request.session["choice_sheet"]    = sheet    = request.GET['choice_sheet']
            request.session["tcp_ip_status"]    = tcp_ip_status    = request.GET['tcp_ip_status']
            request.session["object_status"]    = object_status    = request.GET['object_status']
            request.session["counter_status"]    = counter_status    = request.GET['counter_status']
            
    
    tcp_ip_status="Загрузка портов условно прошла"
    
    
    #print fileName
    args["choice_file"]    = fileName
    args["choice_sheet"]    = sheet
    args["tcp_ip_status"]=tcp_ip_status
    args["object_status"]=object_status
    args["counter_status"]=counter_status
    return render_to_response("service/service_electric.html", args)
    
def load_electric_objects(request):
    args={}
    if request.is_ajax():
        if request.method == 'GET':
            request.session["choice_file"]    = fileName    = request.GET['choice_file']
            request.session["choice_sheet"]    = sheet    = request.GET['choice_sheet']
            request.session["tcp_ip_status"]    = tcp_ip_status    = request.GET['tcp_ip_status']
            request.session["object_status"]    = object_status    = request.GET['object_status']
            request.session["counter_status"]    = counter_status    = request.GET['counter_status']
            
    
    object_status="Загрузка объектов условно прошла"
    
    
    #print fileName
    args["choice_file"]    = fileName
    args["choice_sheet"]    = sheet
    args["tcp_ip_status"]=tcp_ip_status
    args["object_status"]=object_status
    args["counter_status"]=counter_status
    return render_to_response("service/service_electric.html", args)
    
def load_electric_counters(request):
    args={}
    if request.is_ajax():
        if request.method == 'GET':
            request.session["choice_file"]    = fileName    = request.GET['choice_file']
            request.session["choice_sheet"]    = sheet    = request.GET['choice_sheet']
            request.session["tcp_ip_status"]    = tcp_ip_status    = request.GET['tcp_ip_status']
            request.session["object_status"]    = object_status    = request.GET['object_status']
            request.session["counter_status"]    = counter_status    = request.GET['counter_status']
            
    
    counter_status="Загрузка счётчиков условно прошла"
    
    
    #print fileName
    args["choice_file"]    = fileName
    args["choice_sheet"]    = sheet
    args["tcp_ip_status"]=tcp_ip_status
    args["object_status"]=object_status
    args["counter_status"]=counter_status
    return render_to_response("service/service_electric.html", args)
