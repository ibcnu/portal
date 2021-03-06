"""
Django settings for portal project.
Generated by 'django-admin startproject' using Django 2.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/[ref || topics]/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@eq8lnd)4r3bg_aem9no7qp5x=bt@*5t=5p$(sq!w%g2p0b+j&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'crispy-form-tags',
    'widget_tweaks',
    # 'django.contrib.sites',
    # 'django_comments_xtd',
    # 'django_comments',

    'portal',
    'apps.accounts',
    'apps.assets',
    'apps.issues',
    'apps.organizations',
    'apps.profiles',
    'apps.users',
]

AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal.urls'

CURRENT_TEMPLATE = 'carbon'  # ['admin_theme', 'sb-admin', 'bs-dashboard', 'carbon']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'portal.wsgi.application'

# COMMENTS_APP = 'django_comments'
# COMMENTS_XTD_MAX_THREAD_LEVEL = 3
# COMMENTS_XTD_CONFIRM_EMAIL = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = '/home/barry/Documents/django/portal/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)


LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'


EMAIL_BACKEND = 'django.core.backends.console.EmailBackend'

# EMAIL_HOST = "smtp.mail.com"
# EMAIL_PORT = "587"
# EMAIL_HOST_USER = "alias@mail.com"
# EMAIL_HOST_PASSWORD = "yourpassword"
# DEFAULT_FROM_EMAIL = "Helpdesk <helpdesk@yourdomain>"
