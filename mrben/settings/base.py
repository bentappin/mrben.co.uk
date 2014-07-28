# Django settings for mrben project.
import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """
    Get the environment variable or return exception.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = u"Set the %s environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)


PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__).decode('utf-8'), '..'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ben Tappin', 'ben@mrben.co.uk'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'mrben.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    # Thirdparty apps.
    'disqus',
    'south',

    # Project apps.
    'mrben.main',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

TWEET_LIMIT = 5
TWITTER_USER = ''
TWITTER_CACHE_TIMEOUT = 120
LASTFM_KEY = ''
LASTFM_SECRET = ''
LASTFM_USER = ''
LASTFM_PWDHASH = ''
LASTFM_CACHE_TIMEOUT = 900
FLICKR_KEY = ''
FLICKR_SECRET = ''
FLICKR_ID = ''
FLICKR_CACHE_TIMEOUT = 1800
DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = ''

ENTRIES_PER_PAGE = 10
FEATURE_SIDEBAR_COUNT = 2
FEED_CACHE_TIMEOUT = 1800

CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_KEY_PREFIX = 'mrben'
