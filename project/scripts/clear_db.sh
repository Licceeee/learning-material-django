rm -rf core/migrations/*
rm -rf user/migrations/*

rm db.sqlite3

python manage.py makemigrations user
# python manage.py makemigrations core
python manage.py migrate
# python manage.py createsuperuser

# python manage.py migrate admin zero
# python manage.py migrate auth zero
# python manage.py migrate contenttypes zero
# python manage.py migrate sessions zero