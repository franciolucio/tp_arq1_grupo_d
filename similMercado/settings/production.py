from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['similmercado.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd54i5id0v8hqg6',
        'USER': 'wwtgkbikejnkep',
        'PASSWORD' : '125ef197eb9ffa8838ea92625d88256d3cc19aecda2f34bfd4524a9fac93fbbd',
        'HOST': 'ec2-34-236-88-129.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

