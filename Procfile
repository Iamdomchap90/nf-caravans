web: gunicorn --chdir src/ core.wsgi -b 0.0.0.0:80 --log-file -
release: python /app/src/manage.py migrate && python /app/src/manage.py collectstatic --no-input
