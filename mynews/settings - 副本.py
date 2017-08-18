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

ALLOWED_HOSTS = []


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
    #'gunicorn',
    #'xadmin',
    #'crispy_forms',
    #'pagination',
   

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
    #'pagination.middleware.PaginationMiddleware'
)

    

ROOT_URLCONF = 'mynews.urls'

WSGI_APPLICATION = 'mynews.wsgi.application'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    ]
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#mysql写法需要写账号密码端口等


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ZH-CN'#中文，1.9以后改成hans

TIME_ZONE = 'Asia/Shanghai'#时区

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)#模板路径设置。

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),   
)
#静态文件路径

STATIC_ROOT = os.path.join(BASE_DIR, 'site_static')
#用于线上发布之后的root，本地开发不需要

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')#媒体文件路径
MEDIA_URL = '/media/'
#媒体文件主要是用户上传的文件

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

LOGIN_URL= '/login/'
#用户
AUTH_PROFILE_MODULE = 'news.UserProfile' 
ANONYMOUS_USER_ID=-1
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)