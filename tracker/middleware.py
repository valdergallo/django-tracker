from django.conf import settings
from models import *
from views import track
"""
    Authors 
    Google Track http://lethain.com/entry/2007/jun/14/a-django-middleware-for-google-analytics-repost/
    Correct by valdergallo@gmail.com
    Track actions by Valder Gallo valdergallo@gmail.com
"""

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



class GoogleAnalyticsMiddleware(object):
    def __init__(self):
        """
        Constructor for GoogleAnalyticsMiddleware
        
        Instalation:
            Add on settings.py
            ANALYTICS_ID = 'UI-xxxxx-xx'
            
        If you want ignore admin urls use:
            ANALYTICS_IGNORE_ADMIN = True
             
        """
        self.analytics = False
        id = getattr(settings, 'ANALYTICS_ID' , False)
        if id:
            self.html = self.form_analytics_string(id)
            self.analytics = True
            self.ignore_admin = getattr(settings, 'ANALYTICS_IGNORE_ADMIN' , False)


    def process_response(self, request, response):
        """
        Find tag </body> on html and insert google analytics code before
        """
        if self.analytics:
            content = response.content
            index = content.upper().find('</BODY>')

            if self.ignore_admin and request.user.is_authenticated() and request.user.is_staff:
                return response
            #if not have </body>
            if index == -1:
                #print 'not content add'
                return response
            else:
                #print 'content add'
                response.content = content[:index] + self.html + content[index:]

        return response


    @staticmethod
    def form_analytics_string(id):
        """
            Google Analytics code 
        """
        return """
        <!-- Google Analytics -->
        <script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
        </script>
        <script type="text/javascript">
          _uacct = "%s";
          urchinTracker();
        </script>
        <!-- Fim do Google Analytics -->
        """ % (str(id))
