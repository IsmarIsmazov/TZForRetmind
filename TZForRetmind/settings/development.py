from .base import *

SECRET_KEY = config('SECRET_KEY')
DEBUG = True if config('DEBUG') == 'on' else False

CREATE_APPS = [
    'apps.users',
    'apps.products',
]

INSTALLED_LIBRARY = [
    'jazzmin',
    'rest_framework',
    'drf_yasg',
    "corsheaders",
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'openpyxl'

]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]
INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS
