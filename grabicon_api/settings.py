

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IN_PROD = os.environ.get('IN_PROD')



REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_AUTHENTICATION_CLASSES' : [],
    'DEFAULT_PERMISSION_CLASSES' : [],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}



# SECURITY
SECRET_KEY = os.environ.get('SECRECT_KEY') or '#lsvaod=2=c7z@j+)*5oq1la36#sj7bmg_^p6+p-4et#2%0+z6'
DEBUG = False if IN_PROD else True
SECURE_CONTENT_TYPE_NOSNIFF = True if IN_PROD else False
SECURE_BROWSER_XSS_FILTER = True if IN_PROD else False
SESSION_COOKIE_SECURE = True if IN_PROD else False
CSRF_COOKIE_SECURE = True if IN_PROD else False
X_FRAME_OPTIONS = 'DENY'


ALLOWED_HOSTS = eval(os.environ.get('ALLOWED_HOSTS')) if IN_PROD else ['*']


# Application definition
ADMIN_ENABLED = False

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grabicon_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'grabicon_api.wsgi.application'


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


django_heroku.settings(locals())
