"""
Django settings for mySite project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f65z9#czvv*bm4h!)33l%$(e%3qrv6kg1u$eqio0-0--3z$f8g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'home',
    'register',
    'comment'
]



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'giakinhfullstack@gmail.com'
EMAIL_HOST_PASSWORD = 'giakinh0823'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SOCIALACCOUNT_ADAPTER = 'mySite.myAdapter.MySocialAccountAdapter'


ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_QUERY_EMAIL = True

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
DEFAULT_HTTP_PROTOCOL = "https"

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mySite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'mySite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'giakinh',
        'USER': 'giakinh0823',
        'PASSWORD': 'Danhancach0823',
        'HOST': 'tcp:giakinh0823.database.windows.net',
        'PORT': '1433',
        'OPTIONS': {
            'unicode_results':True,
            'extra_params': 'ClientCharset=utf8',
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}

DATABASE_CONNECTION_POOLING = False


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



AZURE_ACCOUNT_NAME = 'sqlvan3doctgbfyraq'
AZURE_ACCOUNT_KEY = 'prKEJB6mWOBX9EZ9M7I0nND3/1RZOpGoR6n4zAGtY+zGgYYKgk2VhMkyoXPMyHCtuKQgp7SlxQbi0IG9SPPYcA=='


STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'

# DEFAULT_FILE_STORAGE = 'mysite.custom_azure.AzureMediaStorage'
DEFAULT_FILE_STORAGE = 'mySite.custom_azure.AzureMediaStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "http://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/media"

MEDIA_ROOT='http://{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
# AZURE_LOCATION=f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
AZURE_LOCATION = 'giakinh0823'
AZURE_CONTAINER = 'giakinh0823'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    STATIC_DIR,
]


LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTHENTICATION_BACKENDS = ('mySite.loginEmailandUser.EmailBackend',)