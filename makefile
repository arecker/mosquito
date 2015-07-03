all:
	python manage.py migrate
	python manage.py collectstatic --noinput
test:
	python manage.py migrate
	python manage.py test
run:
	python manage.py runserver
migrate:
	python manage.py makemigrations
	python manage.py migrate
