from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_MIDDLEWARE_SECONDS = 0


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mrben_dev',
        'USER': 'mrben_dev',
        'PASSWORD': 'mrben_dev',
        'HOST': '',
        'PORT': '',
    }
}


TWITTER_USER = 'mrben_'
TWITTER_TIMEOUT = 3600
LASTFM_KEY = 'bb5aa97fae99fe60132063d07dc18095'
LASTFM_SECRET = 'e2e768a50015a03f91ce7fcd3be48c78'
LASTFM_USER = 'mrben_'
LASTFM_PWDHASH = '437e7eca1931887d9d6a7088458afd5b'
LASTFM_TIMEOUT = 3600
FLICKR_KEY = 'b2ad176e7a038690fc79d8cb11bcf9ba'
FLICKR_SECRET = '6b251679c402e538'
FLICKR_ID = '33411549@N05'
FLICKR_TIMEOUT = 3600 / 2
DISQUS_API_KEY = 'j23PhNMoYJZwwsyhsriQypzOQJEJd1Q4O6BFv0ng0WnHTm6QjcswooZeDeVcIgbG'
DISQUS_WEBSITE_SHORTNAME = 'mrben'

SECRET_KEY = "*-secret-key-*"
