# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a  copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 444  Castro Street, Suite 900, Mountain View, California, 94041, USA.
# Date: 19/06/2011
# Author: Valder Gallo
# E-mail: valdergallo@gmail.com
# encoding: utf-8

from django.conf import settings
from models import *
from views import track


def check_track(full_path):
    exclude_values = [i.url for i in ExcludeUrl.objects.all()]
    for i in exclude_values:
        if i in full_path:
            return False
    return True


class TrackerMiddleware(object):

    def process_response(self, request, response):
        full_path = request.get_full_path()
        if check_track(full_path):
            track(request)

        return response