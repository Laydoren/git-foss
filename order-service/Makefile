.PHONY: create-structure activate install-dep install test-pytest create-venv create-requirements

create-structure:
	mkdir -p src tests docs
	touch src/.gitkeep tests/.gitkeep
	touch docs/DOMAIN.md README.md .gitignore
	touch setup.py requirements.txt

create-requirements:
	pip3 install pipreqs
	python3 -m pipreqs.pipreqs . --force

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-pytest:
	python3 -m pytest

test: install-dep install test-pytest


