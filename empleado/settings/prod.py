
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['68.183.134.175']
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'juan',
        'PASSWORD': '1698',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
# dentro de la carpeta static estan guardados los archivos estaticos (BOOTSTRAP, FOUNDATION, etc)
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')


MEDIA_URL = '/media/'
# dentro de la carpeta media estan guardados los archivos multimedia (imagenes, musica, etc)
MEDIA_ROOT = BASE_DIR.child('media')
