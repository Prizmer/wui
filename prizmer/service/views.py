from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.core.context_processors import csrf
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Create your views here.

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=150)
    path  = forms.FileField()

def choose_service(request):
    return render_to_response("choose_service.html")

def service_electric(request):
    args={}
    args.update(csrf(request))
    return render_to_response("service/service_electric.html", args)
    
def service_electric_load(request):
    args={}
    data_table=[]

    status='file not loaded'

    if request.method == 'POST':
        f=request.FILES['path']
        form = UploadFileForm(request.POST, request.FILES)
        #form = UploadFileForm(request.FILES)
        print f
        
        print form.as_table()
        print form.is_valid()
        #print unicode(form.errors)
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
    #print 'static/cfg/'+f.name
#'C:/Work/mitino/prizmer
    destination = open(os.path.join(BASE_DIR,'static/cfg/'+f.name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    print 'file load'
    destination.close()