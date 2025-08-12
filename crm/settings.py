
# Django settings for testsite project.

import logging
import os.path
import dj_database_url
import re
import sys

from django.contrib.messages import constants as messages
from decouple import config
from django.urls import reverse_lazy

SECRET_KEY = config('SECRET_KEY')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = os.path.basename(BASE_DIR)
RUN_DIR = os.getcwd()

TEMPLATE_REVERT_TO_DJANGO = True
SEND_EMAIL = True
EMAIL_SUBJECT_PREFIX = '[%s] ' % APP_NAME
EMAILER_BACKEND = 'extended_templates.backends.TemplateEmailBackend'
LOCALE_PATHS = (os.path.join(BASE_DIR, APP_NAME, 'locale'),)
DEBUG = config('DEBUG')
FEATURES_DEBUG = True
ACCOUNT_ACTIVATION_DAYS = 2

ALLOWED_HOSTS = ['127.0.0.1', '35.181.86.138', '.onrender.com']

# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
AUTHENTICATION_BACKENDS = ['authentication.models.EmailBackend']
LOGIN_URL = reverse_lazy('login')
# XXX otherwise logout on djaoapp might lead to 410.
LOGIN_REDIRECT_URL = '/'


INSTALLED_APPS = (
	'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.humanize',
    'django.contrib.admin',
    'crm',
    'authentication',
    'dashboard',
    'proprietes',
    'proprietaires',
    'operations',
    'clients',
    'settings',
    'wkhtmltopdf',
)
# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'crm.wsgi.application'
ROOT_URLCONF = 'crm.urls'
# WKHTMLTOPDF_CMD = os.path.join(os.environ["ProgramFiles"],"wkhtmltopdf\bin\wkhtmltopdf.exe")
WKHTMLTOPDF_CMD = "/usr/local/bin/wkhtmltopdf"
WKHTMLTOPDF_CMD_OPTIONS  = {'quiet': True, 'enable-local-file-access': True}

#GRAPPELLI_INDEX_DASHBOARD = 'administration.dashboard.CustomIndexDashboard'

KEEP_LOGGED_DURATION= 30

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/data/db.sqlite3',  # Stockage dans le volume persistant
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
PASSWORD_RESET_TIMEOUT_DAYS = 3650
DISABLE_COLLECTSTATIC = 1
# Static files (CSS, JavaScript, Images)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

PDF_DIR = '/media/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Casablanca'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-Fr'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Allow user to enter month in durationfield
DURATIONFIELD_ALLOW_MONTHS = True

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crm', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',  # because of admin/
                'django.contrib.messages.context_processors.messages',  # because of admin/
                'django.template.context_processors.request',
                'django.template.context_processors.media',
            ],
            'builtins': [
                'crm.templatetags.has_perms']
        }
    }
]


EMAIL_SUBJECT_PREFIX = '[%s] ' % APP_NAME
EMAILER_BACKEND = 'extended_templates.backends.TemplateEmailBackend'



db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_SSL = config('EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
DEFAULT_TO_EMAIL = config('DEFAULT_TO_EMAIL')
DEFAULT_TECHNIQUE_TO_EMAIL = config('DEFAULT_TO_EMAIL')





GRAPPELLI_ADMIN_TITLE = "CRM-LNA-DOR"
