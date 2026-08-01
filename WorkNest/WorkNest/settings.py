from pathlib import Path
#import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------
# SECURITY
# -------------------------------
# Use environment variable (Render)
SECRET_KEY =  'django-insecure-thx8&5!&g@44(ynmp93te23f++17y#=p9$vp)y8y33t1vx)$n^'

DEBUG = True

ALLOWED_HOSTS = []


# -------------------------------
# APPLICATIONS
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'corsheaders',
    'rest_framework',
]


# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # moved up
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'WorkNest.urls'
WSGI_APPLICATION = 'WorkNest.wsgi.application'


# -------------------------------
# DATABASE
# -------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "worknest",
        "USER": "postgres",
        "PASSWORD": "postgreSQL",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# -------------------------------
# CORS / CSRF
# -------------------------------
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = []

CSRF_TRUSTED_ORIGINS = []

CORS_ALLOW_CREDENTIALS = True


# -------------------------------
# STATIC FILES
# -------------------------------
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# -------------------------------
# CUSTOM USER MODEL
# -------------------------------
AUTH_USER_MODEL = 'app.User'


# -------------------------------
# INTERNATIONALIZATION
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
