install:
	pip install -e .['dev']

test:
	pytest tests -v

run:
	export FLASK_APP=delivery/app.py FLASK_ENV=development flask run