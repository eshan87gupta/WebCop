"""
Django settings for WebCop project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hb(ahs+l0)8tfsob@95!worrxmge7(814jfkt=qgb^1+1vfqfc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '192.168.42.231']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'push_notifications',
    'rest_framework',
    'copapp'
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

ROOT_URLCONF = 'WebCop.urls'

PUSH_NOTIFICATIONS_SETTINGS = {
        "FCM_API_KEY": "AIzaSyB_aVApVKq1UFY-GRhKEAyAr5C4VvQ0xKg",
        "GCM_API_KEY": "AIzaSyB_aVApVKq1UFY-GRhKEAyAr5C4VvQ0xKg",
        "APNS_CERTIFICATE": "/path/to/your/certificate.pem",
        "APNS_TOPIC": "com.example.push_test",
        "WNS_PACKAGE_SECURITY_ID": "[your package security id, e.g: 'ms-app://e-3-4-6234...']",
        "WNS_SECRET_KEY": "[your app secret key, e.g.: 'KDiejnLKDUWodsjmewuSZkk']",
        "WP_PRIVATE_KEY": "/path/to/your/private.pem",
        "WP_CLAIMS": {'sub': "mailto: development@example.com"}
}

GCM_APIKEY = "AIzaSyB_aVApVKq1UFY-GRhKEAyAr5C4VvQ0xKg"

GCM_ANDROID_APIKEY ="AIzaSyB_aVApVKq1UFY-GRhKEAyAr5C4VvQ0xKg"

GCM_DEVICE_MODEL = "copapp.Device"

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

WSGI_APPLICATION = 'WebCop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': 'policedb',
        #'USER': 'super',
        #'HOST': 'eshan-797.postgres.pythonanywhere-services.com',
        #'PASSWORD':'padmanabh@2017',
        #'PORT': '10797',


        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'policedb',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PASSWORD':'padamnabh',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'