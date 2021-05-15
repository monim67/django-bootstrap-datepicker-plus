.PHONY: dev docs build

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements/dev.txt
	python dev/manage.py migrate

dev:
	python dev/manage.py runserver

docs:
	make -C docs html

lint:
	python -m pylint bootstrap_datepicker_plus tests dev
	python -m black --exclude /migrations/* --check bootstrap_datepicker_plus tests dev
	rstcheck --report warning *.rst docs/*.rst

test:
	python dev/manage.py test tests/ --keepdb

coverage:
	coverage run --source=bootstrap_datepicker_plus dev/manage.py test tests/ --keepdb
	coverage report

build:
	python setup.py sdist bdist_wheel

deploy:
	twine upload --repository testpypi dist/*

deploy-prod:
	twine upload dist/*
