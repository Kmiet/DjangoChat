"""

Django settings for DjangoChat project.



Generated by 'django-admin startproject' using Django 2.0.5.



For more information on this file, see

https://docs.djangoproject.com/en/2.0/topics/settings/



For the full list of settings and their values, see

https://docs.djangoproject.com/en/2.0/ref/settings/

"""



import os

from .secret import DB_SETUP, SEC_KEY, HOSTS, CH_LAYERS



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))





# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/



# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = SEC_KEY



# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False



ALLOWED_HOSTS = HOSTS



# Login redirect

LOGIN_REDIRECT_URL = '/lobby'



AUTH_USER_MODEL = 'DjangoChat.User'

# Application definition



INSTALLED_APPS = [

    'lobby',

    'DjangoChat',

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'channels',

]



MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    #'DjangoChat.middleware.NewSessionMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'DjangoChat.middleware.RoutingMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = 'DjangoChat.urls'



TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': ['views'],

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



WSGI_APPLICATION = 'DjangoChat.wsgi.application'



#SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"



# Database

# https://docs.djangoproject.com/en/2.0/ref/settings/#databases



DATABASES = DB_SETUP



# Password validation

# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators



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

# https://docs.djangoproject.com/en/2.0/topics/i18n/



LANGUAGE_CODE = 'en-us'



TIME_ZONE = 'UTC'



USE_I18N = True



USE_L10N = True



USE_TZ = True



# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/2.0/howto/static-files/

ENV_PATH = os.path.abspath(os.path.dirname(__file__))


STATIC_URL = '/static/'



STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static'),

]



STATIC_ROOT = os.path.join(BASE_DIR, "public/static/")



# Media



MEDIA_URL = '/media/'



MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media/')





# Channels



ASGI_APPLICATION = 'DjangoChat.routing.application'

CHANNEL_LAYERS = CH_LAYERS