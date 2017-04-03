from .base import *  # noqa


ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': { {% if cookiecutter.use_sqlite_as_local_db_engine == 'yes' %}
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{{cookiecutter.repo_name}}.db',{% else %}
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{cookiecutter.repo_name}}',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',{% endif %}
    }
}


# You might want to use sqlite3 for testing in local as it's much faster.
if IN_TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/{{cookiecutter.repo_name}}_test.db',
        }
    }
