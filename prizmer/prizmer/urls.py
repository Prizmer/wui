from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


import general.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', general.views.default),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/' , include('loginsys.urls')),
    url(r'^askue/' , include('general.urls')),
    url(r'^report/', include('AskueReports.urls')),
    url(r'^viz/', include('AskueViz.urls')),
    url(r'^exit/$', general.views.go_out),
    url(r'^service/', include('service.urls')),
)

urlpatterns += staticfiles_urlpatterns()
