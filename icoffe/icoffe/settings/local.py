from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pr6*cvf+vqcyo5&eh^=!_en)hsad9lfszeo3k-((n#7!vw)a1e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# lista blanca
ALLOWED_HOSTS = []

INSTALLED_APPS += []

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}