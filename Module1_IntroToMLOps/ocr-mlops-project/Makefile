.PHONY: install test lint format all

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:

	python -m pytest --rootdir=. --ignore=venv --tb=short

lint:
	pylint --disable=C0114,C0115,C0116 src

format:
	python -m black src tests

all: install lint test format
