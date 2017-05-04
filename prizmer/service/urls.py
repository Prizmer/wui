# coding -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^test/$', views.choose_service), # Выберите отчет
    url(r'^service_electric/$', views.service_electric), # электрика, загрузка нужных полейъ
    url(r'^service_electric_load/$', views.service_electric_load), # электрика прогрузка
#    url(r'^electric/$', views.electric),
   

)
