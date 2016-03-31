import os
import sys
import site
import urllib
import locale
locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
sys.stdout = sys.stderr

# Project root
root = '/usr/home/{{ project_name }}/{{ project_name }}'
sys.path.insert(0, root)

# Packages from virtualenv
activate_this = '/usr/home/{{ project_name }}/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# Set environmental variable for Django and fire WSGI handler
os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.settings.current'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
