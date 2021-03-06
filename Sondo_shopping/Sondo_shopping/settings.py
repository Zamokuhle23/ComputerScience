

import os

from django.core.checks import templates
import django
# django.setup()

LOGIN_REDIRECT_URL = ('/')

# CELERY_BROKER_URL = 'amqp://rabbitmq'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l!t+dmzf97rt9s*yrsux1py_1@odvz1szr&6&m!f@-nxq6k%%p'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'customers.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'users.apps.UsersConfig',
    'customers',
    'store',
    'users',
    'django_celery_beat',
    'rest_framework',
    'rest_framework_swagger',
    'channels',
    'crispy_forms',
    'rest_auth',
    'djcelery_email',
    'django_celery_results',
    'celery',
    'allauth',

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

ROOT_URLCONF = 'Sondo_shopping.urls'

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
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)
WSGI_APPLICATION = 'Sondo_shopping.wsgi.application'
ASGI_APPLICATION = "Sondo_shopping.asgi.application"


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
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


STATIC_URL = '/static/'
STATIC_FILES = [
    os.path.join('BASE_DIR', 'static')
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
MEDIA_URL = '/media/image/'
MEDIA_ROOT = BASE_DIR

#BROKER_URL = 'amqps://gaseksfj:r52N1lokS5f-eISGcZt_hMEaUt8gEK_f@chimpanzee.rmq.cloudamqp.com/gaseksfj'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'djsbusiso2021@gmail.com'
EMAIL_HOST_PASSWORD = 'taqqlnaidwaoqwoj'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'djsbusiso2021@gmail.com'
CELERY_EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
LOGIN_URL = 'login'
# celery setting.
CELERY_CACHE_BACKEND = 'default'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
CELERY_BROKER_URL = 'redis://localhost:6379'
AUTH_USER_MODEL = "users.User"