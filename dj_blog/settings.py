# import django_heroku

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-_tg9pl*$-)@d2+-ctyr4v1%di=1abxuj&$nbb-9avd+fuuuin'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# FOR PRODUCTION RUN ; YOU NEED TO ADD THE ALLOWED HOST
# E.G  ALLOWED_HOSTS = ['aiziksinfotech.com' , '127.0.0.1']

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'knox',
    'account',

    'django_summernote',
    'corsheaders',
    'blog',
    
    


]



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend/build/'],
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

WSGI_APPLICATION = 'dj_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogger',        
        'USER' : 'postgres',
        'PASSWORD' : 'aiziks',
        'HOST' : 'localhost',
        'PORT' : '5432'

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#static files for development
STATICFILES_DIRS =  BASE_DIR / 'frontend/build/static/',
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# static files for production
# STATIC_ROOT =  BASE_DIR/'frontend/build/static'  

MEDIA_URL = '/media/'  #path to the file in frontend production
MEDIA_ROOT =  BASE_DIR /'media/' #path to frontend production files and images storage

# print(MEDIA_URL)
# print(MEDIA_ROOT)



REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ], # drf permission classes for django rest framework permission configuration

    #DJANGO REST FRAMEWORK DEFAULT AUTHENTICATION CLASS DEFINITION => USING THE "KNOX token authentication"
    # 'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 4

}


from datetime import timedelta
# from rest_framework.settings import api_settings
# from time import gmtime, strftime
# REST_KNOX = {
#   'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
#   'AUTH_TOKEN_CHARACTER_LENGTH': 64,
#   'TOKEN_TTL': timedelta(hours=10),
# #   'USER_SERIALIZER': 'knox.serializers.UserSerializer',
#   'TOKEN_LIMIT_PER_USER': None,
#   'AUTO_REFRESH': True,
# #   'EXPIRY_DATETIME_FORMAT': api_settings.DATETME_FORMAT,
#    'EXPIRY_DATETIME_FORMAT':strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
# }


# rest_framework_simplejst JWT CONF SETTINGS here
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}






# Clickjacking Protection
X_FRAME_OPTIONS = 'SAMEORIGIN'

SUMMERNOTE_THEME = 'bs4'

CORS_ORIGIN_ALLOW_ALL = True




# django-heroku
# django_heroku.settings(locals())