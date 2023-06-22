import os
from pathlib import Path
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.


#DEJO COMENTADO EL BASE DIR POR QUE UTILIZARE OTRO Y ASI TENGO BACKUP

#BASE_DIR = Path(__file__).resolve().parent.parent  
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p2i=7*s^jldvcj-&y+f^n=dtn2bnjd(r7^ry%_t$5+b3wzjmxz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'acceso',
    'carrito',
    'home',
    'tienda',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'notadjango.urls'

#COMENTO EL DIRECTORIO DE ORIGEN PARA DARLE TRATAMIENTO
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

TEMPLATES = [
    {
        # Configuración del backend de las plantillas
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Directorios donde se buscarán las plantillas
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Directorio 'templates' en el directorio base del proyecto
            #SI QUIERES USAR UTILIDADES DEBES DESCOMENTAR LA SIGUIENTE LINEA 
            #Y CREAR EL DIRECTORIO
           #os.path.join(BASE_DIR, 'utilidades'),  # Directorio 'utilidades' en el directorio base del proyecto
        ],

        # Habilitar búsqueda de plantillas en los directorios de las aplicaciones
        'APP_DIRS': True,

        # Opciones adicionales para el backend de las plantillas
        'OPTIONS': {
            'context_processors': [
                # Procesadores de contexto que se aplicarán a las plantillas
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'notadjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#NO OLVIDAR QUE ESTO ESTA COMENTADO COM BACKUP

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yukidata',
        'USER': 'root',
        'PASSWORD': '', #si pide pasword es root sino es en blanco
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-es'#para ponerlo a español españa

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
