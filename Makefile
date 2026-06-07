VENV = .venv

ifeq ($(OS),Windows_NT)
	PYTHON = $(VENV)/Scripts/python.exe
	PIP = $(VENV)/bin/pip
else
	PYTHON = $(VENV)/bin/python
	PIP = $(VENV)/bin/pip
endif

install:
	python -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -e .

run:
	$(PYTHON) -m password_manager.main

check-requirements:
	$(PYTHON) scripts/check_requirements.py

typecheck:
	$(PYTHON) -m mypy src/password_manager tests

test:
	$(PYTHON) -m pytest -v

format:
	$(PYTHON) -m black src/password_manager tests scripts

lint:
	$(PYTHON) -m black --check src/password_manager tests scripts

check: lint typecheck test check-requirements

full-run: install check run