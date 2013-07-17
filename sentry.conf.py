import os
import sys
import logging

from sentry.conf.server import *

ROOT = os.path.dirname(__file__)

sys.path.append(ROOT)

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

# Sentry configuration
# --------------------

SENTRY_KEY = os.environ.get('SENTRY_KEY')

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = int(os.environ.get('PORT', 9000))
SENTRY_WEB_OPTIONS = {
    'workers': 8,
    'worker_class': 'gevent',
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'}
}

# security
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SENTRY_URL_PREFIX = os.environ.get('SENTRY_URL_PREFIX', '')
INSTALLED_APPS += ('djangosecure',)
MIDDLEWARE_CLASSES += ('djangosecure.middleware.SecurityMiddleware',)
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# Email configuration
# -------------------

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Hosts

ALLOWED_HOSTS = [
    '%s.herokuapp.com' % os.environ.get('HEROKU_APP_NAME'),
]

if os.environ.get('CUSTOM_DOMAIN'):
    ALLOWED_HOSTS.append(os.environ.get('CUSTOM_DOMAIN'))


# Disable the default admins (for email)
ADMINS = ()

# Set Sentry's ADMINS to a raw list of email addresses
SENTRY_ADMINS = os.environ.get('ADMINS', '').split(',')

# The threshold level to restrict emails to.
SENTRY_MAIL_LEVEL = logging.WARNING

# The prefix to apply to outgoing emails.
SENTRY_EMAIL_SUBJECT_PREFIX = '[Sentry]'

# The reply-to email address for outgoing mail.
SENTRY_SERVER_EMAIL = os.environ.get('SERVER_EMAIL', 'root@localhost')
