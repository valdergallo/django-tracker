# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a  copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 444  Castro Street, Suite 900, Mountain View, California, 94041, USA.
# Date: 19/09/2010
# Author: Valder Gallo
# E-mail: valdergallo@gmail.com
# encoding: utf-8


from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from models import *
from django.db.models import Count

class TrackerAdmin(admin.ModelAdmin):
    list_display = ('access', 'domain', 'url', 'ip', 'browser')

admin.site.register(Track, TrackerAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ('access', 'domain', 'url', 'ip', 'browser')

admin.site.register(Log, LogAdmin)

admin.site.register(ExcludeUrl)

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'total_track')

    def total_track(self, obj):
        return obj.track_set.all().count() + obj.log_set.all().count()

admin.site.register(Url, UrlAdmin)

class IpAdmin(admin.ModelAdmin):
    list_display = ('ip', 'total_track')

    def total_track(self, obj):
        return obj.track_set.all().count() + obj.log_set.all().count()

admin.site.register(Ip, IpAdmin)

class BrowserAdmin(admin.ModelAdmin):
    list_display = ('browser', 'total_track')

    def total_track(self, obj):
        return obj.track_set.all().count() + obj.log_set.all().count()

admin.site.register(Browser, BrowserAdmin)
