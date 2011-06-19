# Create your views here.

from models import *

def track(request):

    tk_domain = request.META.get('HTTP_HOST', None)
    tk_url = request.get_full_path()
    tk_ip = request.META.get('REMOTE_ADDR', None)
    tk_action = request.META.get('HTTP_REFERER', None)
    tk_browser = request.META.get('HTTP_USER_AGENT', None)

    _domain = Domain.objects.filter(domain=tk_domain)
    if _domain:
        _domain = _domain[0]
    else:
        _domain = Domain.objects.create(domain=tk_domain)

    _ip = Ip.objects.filter(ip=tk_ip)
    if _ip:
        _ip = _ip[0]
    else:
        _ip = Ip.objects.create(ip=tk_ip)

    _browser = Browser.objects.filter(browser=tk_browser)
    if _browser:
        _browser = _browser[0]
    else:
        _browser = Browser.objects.create(browser=tk_browser)


    _url = Url.objects.filter(url=tk_url)
    if _url:
        _url = _url[0]
    else:
        _url = Url.objects.create(url=tk_url)

    return Track.objects.create(domain=_domain, url=_url, ip=_ip, browser=_browser)
