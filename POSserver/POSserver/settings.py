"""
Django settings for POSserver project.
Generated by 'django-admin startproject' using Django 2.1.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from decouple import config
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
            "formatter": "verbose",
        }
    },
    "loggers": {"django": {"handlers": ["file"], "propogate": True, "level": "DEBUG"}},
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")]
)


CORS_ALLOWS_METHODS = ("DELETE", "GET", "OPTIONS", "POST")

CORS_ORIGIN_ALLOW_ALL = True  # Cors Options
CORS_ALLOW_CREDENTIALS = config("CORS_ALLOW_CREDENTIALS", cast=bool, default=False)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# Application definition

INSTALLED_APPS = [
    "server",
    "whitenoise.runserver_nostatic",  # Added for whitenoise
    "django.contrib.staticfiles",  # Added for handling static files
    "django.contrib.admin",
    "django.contrib.auth",
    "graphene_django",  # Added for doing GraphQL
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "corsheaders",  # Added corsheaders
    "django_seed",  # Application to quickly add fake data to the database
    "stripe",
    "sendgrid",
    "payment",
]


GRAPHENE = {"SCHEMA": "POSserver.schema.schema"}  # Where your Graphene schema lives

MIDDLEWARE = [
    "graphql_jwt.middleware.JSONWebTokenMiddleware",  # Added for JWT with graphql
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Added for helping with serving static files
    "corsheaders.middleware.CorsMiddleware",  # Added for cross origin resource
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "POSserver.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "POSserver.wsgi.application"

USER = config("USER")
PASSWORD = config("PASSWORD")
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        "DATABASE_URL",
        default=(
            "postgres://"
            + config("USER")
            + ":"
            + config("PASSWORD")
            + "@"
            + config("PORT")  # 127.0.0.1:5432
            + "/"
            + config("DBNAME")  # posserver
        ),
    )
    # psql posserver -c "GRANT ALL ON ALL TABLES IN SCHEMA public to <username>;"
    # psql posserver -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to <username>;"
    # psql posserver -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to <username>;"
}

AUTH_USER_MODEL = "server.User"


# Authentication Backends - adding for JWT with GraphQL
AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STRIPE_PUBLIC_KEY = "pk_test_VFg2TxWkoz0c2FsJlupSqTsl"


SENDGRID_EMAIL_USERNAME = config("EMAIL_HOST_USER")
SENDGRID_EMAIL_HOST = "smtp.sendgrid.net"
SENDGRID_EMAIL_PASSWORD = "s3ndgr1d"
SENDGRID_EMAIL_PORT = config("SENDGRID_PORT")
EMAIL_USE_TLS = True
SENDGRID_API_KEY = config("SENDGRID_API_KEY")
SERVER_EMAIL = "nphillips78@gmail.com"

CORS_ORIGIN_WHITELIST = config(
    "CORS_ORIGIN_WHITELIST", cast=lambda v: [s.strip() for s in v.split(",")]
)
