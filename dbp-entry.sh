#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

# Start nginx processes
echo Starting nginx
cp ../dbp /etc/nginx/sites-available/dbp
ln -s /etc/nginx/sites-available/dbp /etc/nginx/sites-enabled
systemctl start nginx

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn skhualumni.wsgi:application \
    --name dbp \
    --bind unix:/srv/dbp.sock \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log \
    "$@"

