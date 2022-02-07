DEBUG = False
SECRET_KEY = 'edit and add secret key here'

ALLOWED_HOSTS = ['url without https://']


# Extra deployment settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

ADMINS = (('name', 'email'), )
