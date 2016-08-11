# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.fields import UUIDField

# Create your models here.


class DiagramMainframe(models.Model):
    guid = UUIDField(primary_key=True, max_length=38)
    backgroundurl = models.CharField(max_length=20)
    refreshmentTimeMS = models.IntegerField(default=3000)
    mainframeleft = models.IntegerField()
    mainframetop = models.IntegerField()
    mainframewidth = models.IntegerField()
    mainframeheight = models.IntegerField()
    
    class Meta:
        db_table = 'diagram_mainframe'
        verbose_name = u'Главная диаграмма'
        verbose_name_plural = u'Главные диаграммы'
        
    def __unicode__(self):
        return self.backgroundurl
        
class LinkMainframeAbonents(models.Model):
    guid = UUIDField(primary_key=True, max_length=38)
    guid_abonents = models.ForeignKey('general.Abonents', db_column = 'guid_abonents')
    guid_mainframe = models.ForeignKey('DiagramMainframe', db_column = 'guid_mainframe')
    
    class Meta:
        db_table = 'link_mainframe_abonents'
        verbose_name = u'Привязка абонента к диаграмме'
        verbose_name_plural = u'Привязки абонентов к диаграммам'
        
    def __unicode__(self):
        return u'%s %s' % (self.guid_abonents.name, self.guid_mainframe.backgroundurl)

class DiagramDevices(models.Model):
    guid = UUIDField(primary_key=True, max_length=38)
    deviceboxleft = models.IntegerField()
    deviceboxtop = models.IntegerField()
    deviceboxwidth = models.IntegerField()
    deviceboxheight = models.IntegerField()

    class Meta:
        db_table = 'diagram_devices'
        verbose_name = u'Устройство на диаграмме'
        verbose_name_plural = u'Устройства на диаграмме'
        
    def __unicode__(self):
        return u'Координаты: %s %s - Высота: %s, Ширина: %s' % (self.deviceboxleft, self.deviceboxtop, self.deviceboxheight, self.deviceboxwidth)
    
class LinkTakenParamDiagramDevices(models.Model):
    guid_taken_params = models.ForeignKey('general.TakenParams', to_field = 'guid', db_column = 'guid_taken_params')
    guid_diagram_devices = models.ForeignKey('DiagramDevices', db_column = 'guid_diagram_devices')
    caption = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    showmain  = models.IntegerField(default=1)
    mvalleft  = models.IntegerField()
    mvalright = models.IntegerField()
    
    class Meta:
        db_table = 'link_taken_param_diagram_devices'
        verbose_name = u'Привязка параметров на диаграмме'
        verbose_name_plural = u'Привязки параметров на диаграмме'
        
    def __unicode__(self):
        return u'%s %s' % (self.caption, self.guid_taken_params.name)
    
        