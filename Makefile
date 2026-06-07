VENV = .venv

ifeq ($(OS),Windows_NT)
	PYTHON = $(VENV)/Scripts/python.exe
	PIP = $(VENV)/Scripts/pip.exe
else
	PYTHON = $(VENV)/bin/python
	PIP = $(VENV)/bin/pip
endif

install:
	python -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) -m src.main

check-requirements:
	$(PYTHON) scripts/check_requirements.py

typecheck:
	$(PYTHON) -m mypy src tests

test:
	$(PYTHON) -m pytest -v

format:
	$(PYTHON) -m black src tests scripts

lint:
	$(PYTHON) -m black --check src tests scripts
