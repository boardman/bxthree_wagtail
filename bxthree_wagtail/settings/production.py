from __future__ import absolute_import, unicode_literals
import os
import dj_database_url
from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']


# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = [
    '*',
    'bxthree.com'
]

# Static asset configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

# Media asset configurarion
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Sentry

RAVEN_CONFIG = {
    'dsn': 'https://39d8ef1e893e498db02216311e690e95:f55df228f80241579bfd96d7227c1861@sentry.io/242480',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}