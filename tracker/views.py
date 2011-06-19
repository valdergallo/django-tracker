# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a  copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 444  Castro Street, Suite 900, Mountain View, California, 94041, USA.
# Date: 19/09/2010
# Author: Valder Gallo
# E-mail: valdergallo@gmail.com
#
# encoding: utf-8

from models import *

def track(request):

    tk_domain = None
    tk_ip = None
    tk_browser = None
    tk_url = None

    if hasattr(request,'META'):
        tk_domain = request.META.get('HTTP_HOST', None)
        tk_url = request.get_full_path()
        tk_ip = request.META.get('REMOTE_ADDR', None)
        tk_browser = request.META.get('HTTP_USER_AGENT', None)

    _domain = Domain.objects.filter(domain=tk_domain)
    if _domain:
        _domain = _domain[0]
    elif tk_domain:
        _domain = Domain.objects.create(domain=tk_domain)

    _ip = Ip.objects.filter(ip=tk_ip)
    if _ip:
        _ip = _ip[0]
    elif tk_ip:
        _ip = Ip.objects.create(ip=tk_ip)

    _browser = Browser.objects.filter(browser=tk_browser)
    if _browser:
        _browser = _browser[0]
    elif tk_browser:
        _browser = Browser.objects.create(browser=tk_browser)

    _url = Url.objects.filter(url=tk_url)
    if _url:
        _url = _url[0]
    elif tk_url:
        _url = Url.objects.create(url=tk_url)

    try:
        track = Track()
        track.domain = _domain
        track.url = _url
        track.ip = _ip
        track.browser = _browser
        track.save()
    except:
        track = None

    return track

