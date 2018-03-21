from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['portal.barryhuffman.ca', 'portal.cmssi.com', ]

# INSTALLED_APPS += ('debug_toolbar', )

AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'CONN_MAX_AGE': 0,
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': 'localhost',
#         'NAME': 'portal',
#         'PASSWORD': 'VpC4!pHe',
#         'PORT': '',
#         'USER': 'portal'
#     }
# }

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media')


EMAIL_BACKEND = 'django.core.backends.console.EmailBackend'
