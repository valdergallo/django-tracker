# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a  copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 444  Castro Street, Suite 900, Mountain View, California, 94041, USA.
# Date: 19/09/2010
# Author: Valder Gallo
# E-mail: valdergallo@gmail.com
# encoding: utf-8


from django.db import models, connection, transaction
from django.conf import settings

if not hasattr(settings, 'DJANGO_TRACKER_RANGER'):
    MAX_RANGER = 1000
else:
    MAX_RANGER = settings.DJANGO_TRACKER_RANGER

class Ip(models.Model):
    ip = models.IPAddressField()

    def __unicode__(self):
        return self.ip


class Browser(models.Model):
    browser = models.CharField(max_length=255)

    def __unicode__(self):
        return self.browser


class Domain(models.Model):
    domain = models.URLField()

    def __unicode__(self):
        return self.domain


class ExcludeUrl(models.Model):
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return self.url

    class Meta:
        verbose_name = "Filtro de url"
        verbose_name_plural = "Filtros de url"


class Url(models.Model):
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return self.url


class Log(models.Model):
    access = models.DateTimeField(auto_now_add=True)
    domain = models.ForeignKey(Domain, null=True, blank=True)
    url = models.ForeignKey(Url, null=True, blank=True)
    ip = models.ForeignKey(Ip, null=True, blank=True)
    browser = models.ForeignKey(Browser, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.access)


def flush_tracker():
    cw = Track.objects.values('id').select_related().count()
    if cw >= MAX_RANGER:
        cursor = connection.cursor()
        cursor.execute("begin transaction")
        cursor.execute("insert into tracker_log select * from tracker_track")
        cursor.execute(
            "delete from tracker_track where id in (select id from tracker_log)")

        if connection.is_managed():
            cursor.execute("commit")

        if settings.DEBUG:
            print '\n Flush track - EVIL MODE '


class Track(models.Model):
    access = models.DateTimeField(auto_now_add=True)
    domain = models.ForeignKey(Domain, null=True, blank=True)
    url = models.ForeignKey(Url, null=True, blank=True)
    ip = models.ForeignKey(Ip, null=True, blank=True)
    browser = models.ForeignKey(Browser, null=True, blank=True)

    def save(self, *args, **kwargs):
        flush_tracker()
        super(Track, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return unicode(self.access)