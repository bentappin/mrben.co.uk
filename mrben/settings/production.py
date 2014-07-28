from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mrben_prod',
        'USER': 'mrben_prod',
        'PASSWORD': 'peripatetic',
        'HOST': '',
        'PORT': '',
    }
}

# Absolute path to the directory that holds media.
MEDIA_ROOT = '/var/git/repositories/mrben/static'

SECRET_KEY = get_env_variable('SECRET_KEY')
