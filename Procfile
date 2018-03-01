web: gunicorn config.wsgi:application
worker: celery worker --app=mytime_web.taskapp --loglevel=info
