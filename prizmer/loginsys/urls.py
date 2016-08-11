# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import loginsys.views

urlpatterns = patterns('',
    # Examples:
   url(r'^login/$', loginsys.views.login),
   url(r'^logout/$', loginsys.views.logout),


)

urlpatterns += staticfiles_urlpatterns()