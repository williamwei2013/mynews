# -*- coding: utf-8 -*-
"""
Django settings for mynews project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's59v5_vx2ea-(00fc=l+i*t7^=4tscdj$9mjz$8f8j%136kwjf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['bhshequ.com']#由于没有这个设置，导致nginx一直报400错误无法访问。


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'news',
    'gunicorn',
    

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mynews.urls'

WSGI_APPLICATION = 'mynews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mynews',
        'USER':'root',
        'PASSWORD':'e1de68fb4c',
        'HOST':'127.0.0.1',
        'PORT':'3306',                    
        'unix_socket':'/tmp/mysql.sock',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ZH-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/



TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)#模板路径设置。

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),   
#)
STATIC_ROOT = '/alidata/www/mynews/site_static/'

STATIC_URL = '/site_static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
