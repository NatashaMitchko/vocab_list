#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$FLASK_DEBUG" = "1" ]
then
    pip3 install -r $DEV_REQUIREMENTS

    echo "Creating the database tables..."
    python manage.py create_db
    echo "Done"
    echo "Seeding database..."
    python manage.py seed_db
    echo "Done"
    echo "Tables created"
fi

exec "$@"
