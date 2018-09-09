"""
Django settings for us3000 project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from cloghandler import ConcurrentRotatingFileHandler

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6@tdg=huj#)l&8lsd@uyh)!(p6ui3q_vyq5a=z%p&(ereyzb88'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'words',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(os.path.join(BASE_DIR, 'static')),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Oxford Dictionary configuration variables
# https://developer.oxforddictionaries.com/

OXFORD_DICTIONARY_APP_ID = ''

OXFORD_DICTIONARY_APP_KEY = ''

# https://docs.djangoproject.com/en/2.1/topics/email/

ADMINS = [('John', 'John@example.com')]

# Logging: https://docs.djangoproject.com/en/2.1/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'unsaved_words': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'forvo_log': {
            'level': 'INFO',
            'class': 'logging.handlers.ConcurrentRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'forvo.log'),
            'formatter': 'unsaved_words',
            'maxBytes': 1024*1024,
            'backupCount': 3
        },
        'od_log': {
            'level': 'INFO',
            'class': 'logging.handlers.ConcurrentRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'od.log'),
            'formatter': 'unsaved_words',
            'maxBytes': 1024*1024,
            'backupCount': 3
        },
        'od_convert_log': {
            'level': 'INFO',
            'class': 'logging.handlers.ConcurrentRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'od_convert.log'),
            'formatter': 'unsaved_words',
            'maxBytes': 1024*1024,
            'backupCount': 3
        },
        'pronunc_convert_log': {
            'level': 'INFO',
            'class': 'logging.handlers.ConcurrentRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs',
                                     'pronunce_convert.log'),
            'formatter': 'unsaved_words',
            'maxBytes': 1024 * 1024,
            'backupCount': 3
        },
        'general_log': {
            'level': 'INFO',
            'class': 'logging.handlers.ConcurrentRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'general.log'),
            'formatter': 'default',
            'maxBytes': 1024*1024,
            'backupCount': 3
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'syslog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'default',
            'address': '/dev/log'
        },
        'mail_admin': {
            'level': 'DEBUG',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'default',
            'include_html': True
        }
    },
    'loggers': {
        'forvo_fails': {
            'handlers': ['forvo_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'od_fails': {
            'handlers': ['od_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'od_convert_fails': {
            'handlers': ['od_convert_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'pronunc_convert_fails': {
            'handlers': ['pronunc_convert_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'general': {
            'handlers': ['general_log', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
