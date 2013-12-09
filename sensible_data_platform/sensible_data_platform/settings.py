# Django settings for sensible_data_platform project.

import os
import LOCAL_SETTINGS
import utils.SECURE_platform_config as SECURE_platform_config
import sys

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
LANGUAGE_CODE = 'da'
LANGUAGES = (
	('da', 'Danish'),
	('en', 'English'),
)


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
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
    'sensible_data_platform.context_processors.platform',
    'accounts_social.context_processors.backends',
    # 'social.apps.django_app.context_processors.backends',
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
    'accounts_social',
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
    'django.contrib.auth.backends.ModelBackend',

    # Full list of current providers
    # 'social.backends.open_id.OpenIdAuth',
    # 'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    # 'social.backends.google.GoogleOAuth',
    # 'social.backends.google.GooglePlusAuth',
    'social.backends.twitter.TwitterOAuth',
    # 'social.backends.yahoo.YahooOpenId',
    # 'social.backends.stripe.StripeOAuth2',
    # 'social.backends.persona.PersonaAuth',
    'social.backends.facebook.FacebookOAuth2',
    # 'social.backends.facebook.FacebookAppOAuth2',
    # 'social.backends.yahoo.YahooOAuth',
    # 'social.backends.angel.AngelOAuth2',
    # 'social.backends.behance.BehanceOAuth2',
    # 'social.backends.bitbucket.BitbucketOAuth',
    # 'social.backends.box.BoxOAuth2',
    # 'social.backends.linkedin.LinkedinOAuth',
    # 'social.backends.linkedin.LinkedinOAuth2',
    # 'social.backends.github.GithubOAuth2',
    # 'social.backends.foursquare.FoursquareOAuth2',
    # 'social.backends.instagram.InstagramOAuth2',
    # 'social.backends.live.LiveOAuth2',
    # 'social.backends.vk.VKOAuth2',
    # 'social.backends.dailymotion.DailymotionOAuth2',
    # 'social.backends.disqus.DisqusOAuth2',
    # 'social.backends.dropbox.DropboxOAuth',
    # 'social.backends.evernote.EvernoteSandboxOAuth',
    # 'social.backends.fitbit.FitbitOAuth',
    # 'social.backends.flickr.FlickrOAuth',
    # 'social.backends.livejournal.LiveJournalOpenId',
    # 'social.backends.soundcloud.SoundcloudOAuth2',
    # 'social.backends.thisismyjam.ThisIsMyJamOAuth1',
    # 'social.backends.stocktwits.StocktwitsOAuth2',
    # 'social.backends.tripit.TripItOAuth',
    # 'social.backends.twilio.TwilioAuth',
    # 'social.backends.xing.XingOAuth',
    # 'social.backends.yandex.YandexOAuth2',
    # 'social.backends.douban.DoubanOAuth2',
    # 'social.backends.mixcloud.MixcloudOAuth2',
    # 'social.backends.rdio.RdioOAuth1',
    # 'social.backends.rdio.RdioOAuth2',
    # 'social.backends.yammer.YammerOAuth2',
    # 'social.backends.stackoverflow.StackoverflowOAuth2',
    # 'social.backends.readability.ReadabilityOAuth',
    # 'social.backends.skyrock.SkyrockOAuth',
    # 'social.backends.tumblr.TumblrOAuth',
    # 'social.backends.reddit.RedditOAuth2',
    # 'social.backends.steam.SteamOpenId',
    # 'social.backends.podio.PodioOAuth2',
    # 'social.backends.amazon.AmazonOAuth2',
    # 'social.backends.email.EmailAuth',
    # 'social.backends.username.UsernameAuth',
    # 'social.apps.django_app.utils.BackendWrapper',
)

# Sets the social provider settings provided in SECURE_platform_config (i.e. SOCIAL_AUTH_FACEBOOK_KEY and SOCIAL_AUTH_FACEBOOK_SECRET)
mod_object = sys.modules[__name__]
for provider_name, provider in SECURE_platform_config.SOCIAL_PROVIDERS.iteritems():
    for key,value in provider.iteritems():
        setattr(mod_object, provider_name+'_'+key, value)


SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

# Ask for email from facebook
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE =(
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'accounts_social.pipeline.register',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details' # Comment this out to not pull name-details from social provider
)

import hashlib
SESSION_COOKIE_NAME = str(hashlib.sha1(SECRET_KEY).hexdigest())

LOCALE_PATHS = (
	'/home/arks/sensibledtu_DEVEL/SensibleData-Platform/sensible_data_platform/locale',
)
