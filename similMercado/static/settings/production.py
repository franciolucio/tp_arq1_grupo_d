from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['similmercado.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd57cd1ppkmeajf',
        'USER': 'uhtzfrllujjcug',
        'PASSWORD' : '31dfd15c78d58a7a1c119e51d98308ed7e08ef7c6340344bd09f30baaff0f0ca',
        'HOST': 'ec2-34-202-54-225.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

