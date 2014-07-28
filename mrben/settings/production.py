from .base import *

ALLOWED_HOSTS = ['mrben.co.uk']

WSGI_APPLICATION = 'mrben.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mrben_prod',
        'USER': 'mrben_prod',
        'PASSWORD': get_env_variable('PSQL_PROD_PASS'),
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = get_env_variable('SECRET_KEY')
