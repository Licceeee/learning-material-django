
rm db.sqlite3
rm -rf core/migrations/*
rm -rf user/migrations/*
rm -rf material/migrations/*

python manage.py makemigrations user
python manage.py makemigrations core
python manage.py makemigrations material
python manage.py migrate
python manage.py createsuperuser

# python manage.py migrate admin zero
# python manage.py migrate auth zero
# python manage.py migrate contenttypes zero
# python manage.py migrate sessions zero