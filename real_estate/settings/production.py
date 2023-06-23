from .base import *
from .base import env

ADMINS = [("elijah obara", "elijahobara357@gmail.com")]

#TODO add domain names of the production server
CSRF_TRUSTED_ORIGINS = []

SECRET_KEY = env("DJANGO_SECRET_KEY")

DATABASES = {"default": env.db("DATABASE_URL")}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

# TODO: change to 518400 later
SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_HOST_USER = "realestate@gmail.com"
EMAIL_HOST_PASSWORD = env("SMTP_MAILGUN_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DOMAIN = env("DOMAIN")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}