from django.contrib import admin
from AskueViz.models import DiagramMainframe, LinkMainframeAbonents, DiagramDevices, LinkTakenParamDiagramDevices

# Register your models here.

admin.site.register(DiagramMainframe)
admin.site.register(LinkMainframeAbonents)
admin.site.register(DiagramDevices)
admin.site.register(LinkTakenParamDiagramDevices)