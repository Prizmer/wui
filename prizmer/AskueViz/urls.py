from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^viz_mainframe/$', views.viz_mainframe),
    url(r'^viz_devices/$', views.viz_devices),
    url(r'^energo_schema/$', views.energo_scheme),

    #---- Test urls

   # url(r'^test4/$', views.main_data_json_test),




)
