import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': ':memory:',
        'NAME': os.path.join(BASE_DIR, 'sqlite.db')
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.messages',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'django_select2',
    'tests.testapp',
)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SITE_ID = 1
ROOT_URLCONF = 'tests.testapp.urls'

LANGUAGES = [
    ('de', 'German'),
    ('en', 'English'),
]

MIDDLEWARE = [
    #'django.middleware.cache.UpdateCacheMiddleware',    # This must be first on the list
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware', # This must be last
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': ['templates'],
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

SECRET_KEY = '123456'

USE_L10N = True
USE_I18N = True
