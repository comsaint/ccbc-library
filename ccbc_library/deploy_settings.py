import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

### Deploy. Overwrite settings.
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_PATH = os.path.join(BASE_DIR,'ccbc_library/static')
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#sendgrid, for email
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('sendgrid_username','')
EMAIL_HOST_PASSWORD = os.environ.get('sendgrid_password','')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Turn off DEBUG mode
DEBUG = False

TEMPLATE_DEBUG = False

# Import all of local settings if the file exists
try:
    from .local_settings import *
except ImportError:
    pass