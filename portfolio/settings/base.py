"""
Django settings for portfolio project.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

env = os.environ.copy()

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "portfolio.base",
    "portfolio.pages",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
ROOT_URLCONF = "portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
#
# Using SQLite in production
# Watch https://pretalx.com/djangocon-europe-2023/talk/J98ZTN/ to be convinced!

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    # "static_compiled" is a folder used by the front-end tooling
    # to output compiled static assets.
    # This may not exist yet, but will be automatically created when compiling.
    os.path.join(BASE_DIR, "static_compiled"),
]

STATIC_ROOT = env.get("STATIC_DIR", os.path.join(BASE_DIR, "static"))
STATIC_URL = env.get("STATIC_URL", "/static/")

MEDIA_ROOT = env.get("MEDIA_DIR", os.path.join(BASE_DIR, "media"))
MEDIA_URL = env.get("MEDIA_URL", "/media/")
MEDIA_PREFIX = env.get("MEDIA_PREFIX", "")

# Default storage settings, with the staticfiles storage updated.
# See https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Switch off DEBUG mode explicitly in the base settings.
# https://docs.djangoproject.com/en/stable/ref/settings/#debug
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Secret key should always be set in the environment variable and never added to the repository.
SECRET_KEY = env.get("SECRET_KEY", "set-me-please")

# Wagtail settings.

# Shown on Wagtail admin. Can give different name on prod and staging to avoid confusion.
WAGTAIL_SITE_NAME = env.get("WAGTAIL_SITE_NAME", "Developer Portfolio")

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = env.get("WAGTAILADMIN_BASE_URL", "http://localhost:8000")

# Define what hosts an app can be accessed by.
# https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
if "ALLOWED_HOSTS" in env:
    ALLOWED_HOSTS = env["ALLOWED_HOSTS"].split(",")

# Use custom wagtail models in case we ever need to override the defaults.
# It is much easier to start with a custom model from the beginning
# than to change later.


WAGTAILIMAGES_IMAGE_MODEL = "base.CustomImage"

WAGTAILDOCS_DOCUMENT_MODEL = "base.CustomDocument"
