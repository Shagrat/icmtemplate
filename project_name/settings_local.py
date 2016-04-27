import os

DEBUG = True
SITE_ID = 2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_SERVE_ROOT = os.path.join(BASE_DIR, '../media/')

SITE_HOST = '0.0.0.0:8000'
SITE_URL = 'http://0.0.0.0:8000/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'localhost'
