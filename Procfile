web: gunicorn config.wsgi:application
worker: celery worker --app=djangove.taskapp --loglevel=info
