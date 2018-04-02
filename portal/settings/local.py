from .base import *

SECRET_KEY = '@eq8lnd)4r3bg_aem9no7qp5x=bt@*5t=5p$(sq!w%g2p0b+j&'

DEBUG = True

# ALLOWED_HOSTS = []

# INSTALLED_APPS += ('debug_toolbar', )

AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media')


EMAIL_BACKEND = 'django.core.backends.console.EmailBackend'

try:
    from portal.settings.local import *
except:
    pass
