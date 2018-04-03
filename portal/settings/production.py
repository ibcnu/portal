from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['portal.barryhuffman.ca', 'portal.cmssi.com', '165.227.184.224']

AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'portal.sqlite3'),
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

# EMAIL_HOST = "smtp.mail.com"
# EMAIL_PORT = "587"
# EMAIL_HOST_USER = "@cmssi.com"
# EMAIL_HOST_PASSWORD = "yourpassword"
# DEFAULT_FROM_EMAIL = "Helpdesk <helpdesk@cmssi.com>"

try:
    from portal.settings.local import *
except:
    pass
