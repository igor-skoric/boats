from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-39zplp)er3%6h*wi6v*_g1ku4ioq2&&j1#d-a6!c7oi$5*s!jg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'boats.rs', 'boats.rs.itbranch.rs']


# Application definition

INSTALLED_APPS = [
    'nested_admin',
    'tailwind',
    'theme',
    'website',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise',
    'django_browser_reload',
    'jazzmin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'boats.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'website.context_processors.config',
                'website.context_processors.breadcrumbs',
            ],
        },
    },
]

WSGI_APPLICATION = 'boats.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Putanja gde će se statički fajlovi čuvati u produkciji (nakon komande collectstatic)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Direktori za dodatne statičke fajlove
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Direktori za medijske fajlove
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Tailwind CSS
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.boats.rs'  # SMTP server za vašu domenu (npr. cPanel)
EMAIL_PORT = 587    # Koristi 587 za TLS (ako koristite TLS enkripciju)
EMAIL_USE_TLS = True  # Uključivanje TLS enkripcije (ili False ako ne koristiš TLS)
EMAIL_HOST_USER = 'contact@boats.rs'  # Tvoj email
EMAIL_HOST_PASSWORD = ''  # Tvoj email password (ili aplikacijski password)
DEFAULT_FROM_EMAIL = 'contact@boats.rs'  # Email sa kojeg ćeš slati poruke


LOGGING_DIR = os.path.join(BASE_DIR, "logs")  # Kreiraj folder za logove
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)


# LOGOVI
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "error": {
            "format": "{levelname} {asctime} {pathname}:{lineno} {message}",
            "style": "{",
        },
    },
    "handlers": {
        # Handler za ERROR logove
        "error_file": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOGGING_DIR, "errors.log"),
            "maxBytes": 5 * 1024 * 1024,  # 5MB po fajlu
            "backupCount": 3,  # Čuva poslednja 3 log fajla
            "formatter": "error",
        },
        # Handler za INFO logove
        "info_file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOGGING_DIR, "info.log"),
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 3,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["error_file", "info_file"],
            "level": "INFO",  # Hvatamo i INFO i ERROR logove
            "propagate": True,
        },
    },
}


JAZZMIN_SETTINGS = {
    "site_title": "My Admin Panel",
    "site_header": "My Admin Panel",
    "welcome_sign": "Welcome to My Admin Panel",
    "custom_links": {
        "website": [{
            "name": "Home",
            "url": "/",
            "icon": "fas fa-home",
            "permissions": ["auth.view_user"]
        }]
    },
}