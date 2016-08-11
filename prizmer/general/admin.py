from django.contrib import admin
from general.models import Objects, Abonents, TypesAbonents, Meters, MonthlyValues, DailyValues, CurrentValues, VariousValues, TypesParams, Params, TakenParams, LinkAbonentsTakenParams, Resources, TypesMeters, Measurement, NamesParams, BalanceGroups, LinkMetersComportSettings, LinkMetersTcpipSettings, ComportSettings, TcpipSettings, LinkBalanceGroupsMeters

# Register your models here.
class LinkAbonentsTakenParamsAdmin(admin.ModelAdmin):
    list_select_related = True
    search_fields = [u'name']

class MetersAdmin(admin.ModelAdmin):
    search_fields = [u'name']
    date_hierarchy = 'dt_last_read'
    list_display = (u'name','factory_number_manual', 'dt_last_read', 'is_factory_numbers_equal')
    
class AbonentsAdmin(admin.ModelAdmin):
    search_fields = [u'name', u'account_2']
    
class TakenParamsAdmin(admin.ModelAdmin):
    search_fields = [u'name']
    
class ObjectsAdmin(admin.ModelAdmin):
    search_fields = [u'name']
    
class ParamsAdmin(admin.ModelAdmin):
    search_fields = [u'name']
    
class LinkMetersTcpipSettingsAdmin(admin.ModelAdmin):
    search_fields = [u'guid_meters__factory_number_manual']
    
class LinkMetersComportSettingsAdmin(admin.ModelAdmin):
    search_fields = [u'guid_meters__factory_number_manual']

admin.site.register(Objects, ObjectsAdmin)
admin.site.register(Abonents, AbonentsAdmin)
admin.site.register(TypesAbonents)
admin.site.register(Meters, MetersAdmin)
admin.site.register(MonthlyValues)
admin.site.register(DailyValues)
admin.site.register(CurrentValues)
admin.site.register(VariousValues)
admin.site.register(TakenParams, TakenParamsAdmin)
admin.site.register(Resources)
admin.site.register(TypesMeters)
admin.site.register(Measurement)
admin.site.register(NamesParams)
admin.site.register(Params, ParamsAdmin)
admin.site.register(TypesParams)
admin.site.register(BalanceGroups)
admin.site.register(LinkAbonentsTakenParams, LinkAbonentsTakenParamsAdmin)
admin.site.register(LinkMetersComportSettings, LinkMetersComportSettingsAdmin)
admin.site.register(LinkMetersTcpipSettings, LinkMetersTcpipSettingsAdmin)
admin.site.register(ComportSettings)
admin.site.register(TcpipSettings)
admin.site.register(LinkBalanceGroupsMeters)