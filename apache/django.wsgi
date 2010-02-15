import os
import sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'mrben.settings'
sys.path.append('/var/git')
sys.path.append('/var/git/mrben-site/thirdparty')
application = django.core.handlers.wsgi.WSGIHandler()

