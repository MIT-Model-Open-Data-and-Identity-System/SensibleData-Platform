# Django settings for sensible_data_platform project.

import os
import LOCAL_SETTINGS

DEBUG = True
TEMPLATE_DEBUG = DEBUG
MAINTENANCE_MODE = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
BASE_DIR = LOCAL_SETTINGS.BASE_DIR
ROOT_DIR = LOCAL_SETTINGS.ROOT_DIR
ROOT_URL = LOCAL_SETTINGS.ROOT_URL
DATABASES = LOCAL_SETTINGS.DATABASES
BASE_URL = LOCAL_SETTINGS.BASE_URL
TRUST_ROOTS = LOCAL_SETTINGS.TRUST_ROOTS

PLATFORM_NAME = LOCAL_SETTINGS.PLATFORM_NAME
SUPPORT_EMAIL = LOCAL_SETTINGS.SUPPORT_EMAIL

SOCIAL_AUTH_FACEBOOK_KEY = LOCAL_SETTINGS.SOCIAL_AUTH_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = LOCAL_SETTINGS.SOCIAL_AUTH_FACEBOOK_SECRET

MAINTENANCE_IGNORE_URLS = (
		    r'^.*/admin/$',
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

LOGIN_URL = ROOT_URL + 'accounts/login/'
LOGIN_REDIRECT_URL = ROOT_URL

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
	# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ROOT_DIR+'static_root/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = ROOT_URL+'static/'

# Additional locations of static files
STATICFILES_DIRS = (
    ROOT_DIR+'static/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = LOCAL_SETTINGS.SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
	'maintenancemode.middleware.MaintenanceModeMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.static',
        'django.contrib.auth.context_processors.auth',
 		'sensible_data_platform.context_processors.platform',
        'social.apps.django_app.context_processors.backends',
        'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'sensible_data_platform.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sensible_data_platform.wsgi.application'

TEMPLATE_DIRS = (
		ROOT_DIR+'templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'openid_provider',
    'accounts',
    'render',
    'identity_providers',
    'utils',
    'oauth2app',
    'oauth2_authorization_server',
    'uni_form',
    'service_manager',
    'south',
    'sensible_platform_documents',
    'social.apps.django_app.default',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Used by social auth
USERNAME_IS_FULL_EMAIL = True

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    # 'social.backends.facebook.FacebookAppOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    # 'social.backends.open_id.OpenIdAuth',
    # 'social.backends.google.GoogleOpenId',
    # 'social.backends.google.GoogleOAuth2',
    # 'social.backends.google.GoogleOAuth',
    # 'social.backends.twitter.TwitterOAuth',
)

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE =(
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'accounts.social_pipeline.register',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

import hashlib
SESSION_COOKIE_NAME = str(hashlib.sha1(SECRET_KEY).hexdigest())
