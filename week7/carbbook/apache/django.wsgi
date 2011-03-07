import os
import sys

sys.path.append('/home/mcloudx/Python-Class/week7')
sys.path.append('/home/mcloudx/Python-Class/week7/carbbook')

os.environ['DJANGO_SETTINGS_MODULE'] = 'carbbook.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

