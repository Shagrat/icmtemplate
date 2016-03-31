from .base import *

DEBUG = True
SITE_ID = 2

STATIC_SERVE_ROOT = os.path.join(BASE_DIR, '../../media/')

SITE_HOST = '0.0.0.0:8000'
SITE_URL = 'http://0.0.0.0:8000/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'localhost'
