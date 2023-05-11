
ROOT_URLCONF = 'core.urls'

# All apps
INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Thirdparty Libs
    'corsheaders',
    'rest_framework',
    'drf_spectacular',
    'rest_framework.authtoken',
    'django_rest_passwordreset',
    'phonenumber_field',
    'simple_history',

    # Modules Apps
    'users',
    'products',
    'orders',
    'baton.autodiscover',

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'centribaldb',
        'USER': 'centribaluser',
        'PASSWORD': '5nFyHgRtx8z3Mf5kcar8d2D4yQrVgFE2',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
