"""
Django settings for SuperTasks project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xv9uwn3qkkw73h(_wi-3%fpz^83o$)6odi4!g7*god#@7gogf#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'osu-cs361-supertasks.uc.r.appspot.com',
    'osu-cs361-supertasks.appspot.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Run "python -m pip install django-widget-tweaks" if this doesn't load
    'widget_tweaks',
    #project apps
    'accounts.apps.AccountsConfig', #allow accounts/signals.py to work
    'projects',
    'teams',
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

ROOT_URLCONF = 'SuperTasks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")], #add template folder within each App
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

WSGI_APPLICATION = 'SuperTasks.wsgi.application'

# Set this to True when running migrations on the Google Cloud SQL database
# See DATABASE_MIGRATION_README.md for more information.
USE_CLOUD_SQL_PROXY = False

if os.getenv('GAE_APPLICATION', None):
    DEBUG = False
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/osu-cs361-supertasks:us-central1:osu-cs361-supertasks',
            'USER': 'django',
            'PASSWORD': 'django',
            'NAME': 'supertasks',
        }
    }
elif USE_CLOUD_SQL_PROXY is True:
    # Connect to Google Cloud SQL via the proxy.
    # See DATABASE_MIGRATION_README.md for information on how to connect the proxy.
    #
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'supertasks',
            'USER': 'django',
            'PASSWORD': 'django',
        }
    }
else:
    # Built-in SQLite database for local development
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


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

"""Static Media Configuration"""
STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, "static/images")

# Authentication settings
LOGIN_REDIRECT_URL = '/'

# Uncomment if we need to change from this default
# LOGIN_URL = '/accounts/login'

# Uncomment if we need a logout redirect URL
# LOGOUT_REDIRECT_URL = '........'

# Use Google Cloud Storage bucket for media when running in Google Cloud
# This overrules the local "/images/" directory for media.
if os.getenv('GAE_APPLICATION', None):
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'osu-cs361-supertasks.appspot.com'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './osu-cs361-supertasks-f97d63097624.json'
    
    # Leave this commented unless we want to use the Google Cloud Storage bucket for CSS/JS files too
    # That would involve using 'python manage.py collectstatic' during the build process which would
    # upload static files in "/static/" directory to Google Cloud Storage bucket.
    # STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
