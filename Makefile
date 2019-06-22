# Variables
PYTHONPATH := $(shell pwd)

test:
	@pytest -svv --cov=src tests/ --cov-report xml

cov:
	coverage report -m

setup:
	@echo "---- Installing Python Dependencies ----"
	@pip install -r requirements.txt --upgrade

setup_dev:
	@echo "---- Installing Dev Python Dependencies ----"
	@if [[ ! -e .env ]]; then \
		cp .env-example .env ; \
	fi
	@pip install -r requirements-dev.txt --upgrade

run:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}" gunicorn -c ./src/gunicorn.py src.app:app

run_dev:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}" FLASK_ENV=development python ./src/app.py

clean:
	@echo "---- Cleaning up .pyc files ----"
	@find . -name '*.pyc' -delete
	@echo "---- Cleaned ----"

.PHONY: revision
revision:
	alembic revision --autogenerate;

.PHONY: upgrade
upgrade:
	alembic upgrade head

.PHONY: downgrade
downgrade:
	alembic downgrade head
