# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'mediagenerator',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',

    'storeathon',

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',# This is loading other modules, so it goes first because we want everything set before processing.
    'mediagenerator.middleware.MediaMiddleware', # Serves/caches static files with urls starting with DEV_MEDIA_URL 
    'django.middleware.cache.UpdateCacheMiddleware',   # Must be before other middleware that changes the header, so it seems that the right place for this is here
    'google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware', # Must be 'first' too. It collects stats of all middlewares below this. If you want stats from the middlewares above move it to the top

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.csrf.middleware.CsrfViewMiddleware', 
    'django.middleware.csrf.CsrfResponseMiddleware', 
    'django.middleware.cache.FetchFromCacheMiddleware', 
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)

MEDIA_BUNDLES = (
    (   'style.css',
        'css/default.css',
    ),
    (   'js/jcarousellite_1.0.1c5.js',
        'js/jquery-1.5.2.min.js',
    ),
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = os.path.join(os.path.dirname(__file__),'yuicompressor.jar')

MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/devmedia/'
PRODUCTION_MEDIA_URL = '/media/'
GLOBAL_MEDIA_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)
ADMIN_MEDIA_PREFIX = '/media/admin/'

ROOT_URLCONF = 'urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'