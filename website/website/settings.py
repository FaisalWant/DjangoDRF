"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from environ import Env 
import os

ENV= Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zf8c#tl-o@j#5s95&nreo!h4aoecbeg2s&3vxhi9vh#zoi1q-n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["10.0.2.15","127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testapp',
    'blog',
    'rest_framework',
    'django_extensions',
    'organizer',
    'user'
]



SHELL_PLUS="ipython"

SHELL_PLUS_PRINT_SQL= True 

NOTEBOOK_ARGUMENTS=[
"--ip", 
"0.0.0.0",
"--port", 
"8888", 
"--allow-root", 
"--no-browser"

]

IPYTHON_ARGUMENTS =[
    "--ext", 
    "django_extensions.management.notebook_extension",
    "--debug"
    ]

IPYTHON_KERNEL_DISPLAY_NAME= "Django Shell-Plus"

SHELL_PLUS_POST_IMPORTS = [ # extra things to import in notebook
    ("module1.submodule", ("func1", "func2", "class1", "etc")),
    ("module2.submodule", ("func1", "func2", "class1", "etc"))

]

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true" # only use in developmen


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {"default": ENV.db("DATABASE_URL")}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators


AUTH_USER_MODEL="user.User"
AUTH_P= "django.contrib.auth.password_validation."


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': AUTH_P+"UserAttributeSimilarityValidator",
        'OPTIONS':{
        "user_attributes":{
        "email",
        "full_name",
        "short_name",
        }
        }
    },




    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': AUTH_P+"NumericPasswordValidator",
    },
]

LOGIN_URL="auth:login"
LOGIN_REDIRECT_URL="site_root"
LOGOUT_REDIRECT_URL="auth:login"



PASSWORD_HASHERS =[
    "django.contrib.auth.hashers.Argon2PasswordHasher", 
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",



]
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


 STATIC_ROOT = BASE_DIR("runtime", "static")
 STATIC_URL = "/static/"
 STATICFILES_STORAGE = (
     "django.contrib.staticfiles.storage.StaticFilesStorage"
 )
 
 EMail configuration5 EMAIL_BACKEND = ENV.str(
     "EMAIL_BACKEND",
     default="django.core.mail.backends.console.EmailBackend",
 )


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
