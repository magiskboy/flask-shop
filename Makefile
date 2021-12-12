deps:
	pip install -r requirements.txt

dev:
	@export FLASK_APP=wsgi:app
	@export FLASK_ENV=development
	flask run

start:
	@export FLASK_ENV=production
	gunicorn -c gunicorn.config.py wsgi:app