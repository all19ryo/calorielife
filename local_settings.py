import os

# SECRET_KEY = 'rlozw&wtvh2m9*%53q8qcvs1o1ay=bz^4!w!b)nz6#87t2$z(c'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True