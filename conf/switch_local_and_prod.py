LOCAL = True
# SECRET_KEY = 'w+=!lhwq)r=faead(%eojd=(vd7^nqrqh-#79!82=%d9%p!!8y'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
