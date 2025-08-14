.PHONY: install test lint format all

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest -q

lint:
	pylint --disable=C0114,C0115,C0116 src

format:
	black src tests

all: install lint test format
