from skhualumni.settings import *

DEBUG = False
ALLOWED_HOSTS = ['dbp.harveyk.me', 'localhost', ]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'skhualumni',
        'USER': 'root',
        'PASSWORD': os.getenv('MYSQL_ROOT_PASSWORD'),
        'HOST': 'db',
        'PORT': 3306,
    }
}
