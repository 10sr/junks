# -*- mode: python -*-

import os

LOGIN_URL = "/neru/login/"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.environ["NERU_BASE_DIR"]

ROOT_URLCONF = "proj.urls"

WSGI_APPLICATION = "proj.wsgi.application"

INSTALLED_APPS = [
    "app.apps.AppConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "ja-jp"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/neru/static/"
