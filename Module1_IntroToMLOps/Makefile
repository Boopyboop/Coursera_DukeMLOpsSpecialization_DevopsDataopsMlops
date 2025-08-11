.PHONY: install lint test format all

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

lint:
	pylint --disable=R,C hello.py test_hello.py

test:
	python -m pytest -vv --cov=hello --cov-report=term-missing

format:
	black .

all: install lint test format
