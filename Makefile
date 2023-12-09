SHELL := /bin/bash
PYTHON = python3
PIP = $(PYTHON) -m pip

ifeq ($(OS),Windows_NT)
    ACTIVATE_VENV = venv\Scripts\activate
else
    ACTIVATE_VENV = source venv/bin/activate
endif

ifneq ("$(wildcard .env)","")
    include .env
endif

.PHONY: analyze init pre-commit requirements lint clean test build force-release publish-test publish-prod help

# Default target executed when no arguments are given to make.
all: help

analyze:
	cloc . --exclude-ext=svg,json,zip --vcs=git

# -------------------------------------------------------------------------
# Initialize. create virtual environment and install requirements
# -------------------------------------------------------------------------
init:
	make clean && \
	npm install && \
	python3.11 -m venv venv && \
	$(ACTIVATE_VENV) && \
	pip install --upgrade pip && \
	make requirements

# -------------------------------------------------------------------------
# Install and run pre-commit hooks
# -------------------------------------------------------------------------
pre-commit:
	pre-commit install
	pre-commit run --all-files

# -------------------------------------------------------------------------
# Install requirements: Python, npm and pre-commit
# -------------------------------------------------------------------------
requirements:
	rm -rf .tox
	$(PIP) install --upgrade pip wheel
	$(PIP) install -r requirements/local.txt && \
	npm install && \
	make pre-commit
	pre-commit autoupdate

# -------------------------------------------------------------------------
# Run black and pre-commit hooks.
# includes prettier, isort, flake8, pylint, etc.
# -------------------------------------------------------------------------
lint:
	pre-commit run --all-files && \
	black .

# -------------------------------------------------------------------------
# Destroy all build artifacts and Python temporary files
# -------------------------------------------------------------------------
clean:
	rm -rf venv .pytest_cache __pycache__ .pytest_cache node_modules && \
	rm -rf build dist secure_logger.egg-info

# -------------------------------------------------------------------------
# Run Python unit tests
# -------------------------------------------------------------------------
test:
	python -m unittest discover -s secure_logger/tests/ && \
	python -m setup_test

# -------------------------------------------------------------------------
# Build the project
# -------------------------------------------------------------------------
build:
	@echo "-------------------------------------------------------------------------"
	@echo "                   I. Unit tests"
	@echo "-------------------------------------------------------------------------"
	make test
	@echo "-------------------------------------------------------------------------"
	@echo "                   II. Check version"
	@echo "-------------------------------------------------------------------------"
	npx semantic-release --doctor --dry-run
	@echo "-------------------------------------------------------------------------"
	@echo "                   III. Initializing the project,"
	@echo "                        Linting and running pre-commit hooks"
	@echo "-------------------------------------------------------------------------"
	make init
	. venv/bin/activate
	$(PIP) install --upgrade setuptools wheel twine
	$(PIP) install --upgrade build
	@echo "-------------------------------------------------------------------------"
	@echo "                   IV. Building the project"
	@echo "-------------------------------------------------------------------------"

	$(PYTHON) -m build --sdist ./
	$(PYTHON) -m build --wheel ./

	@echo "-------------------------------------------------------------------------"
	@echo "                   V. Verifying the build"
	@echo "-------------------------------------------------------------------------"
	twine check dist/*

# -------------------------------------------------------------------------
# Force a new semantic release to be created in GitHub
# -------------------------------------------------------------------------
force-release:
	git commit -m "fix: force a new release" --allow-empty && git push

# -------------------------------------------------------------------------
# Publish to PyPi Test
# https://test.pypi.org/project/secure-logger/
# -------------------------------------------------------------------------
publish-test:
	git rev-parse --abbrev-ref HEAD | grep '^main$' || (echo 'Not on main branch, aborting' && exit 1)
	make build
	twine upload --verbose --skip-existing --repository testpypi dist/*

# -------------------------------------------------------------------------
# Publish to PyPi
# https://pypi.org/project/secure-logger/
# -------------------------------------------------------------------------
publish-prod:
	git rev-parse --abbrev-ref HEAD | grep '^main$' || (echo 'Not on main branch, aborting' && exit 1)
	make build
	twine upload --verbose --skip-existing dist/*

# -------------------------------------------------------------------------
# Generate help menu
# -------------------------------------------------------------------------
help:
	@echo '===================================================================='
	@echo 'init			- build virtual environment and install requirements'
	@echo 'analyze			- runs cloc report'
	@echo 'pre-commit		- install and configure pre-commit hooks'
	@echo 'requirements		- install Python, npm and pre-commit requirements'
	@echo 'lint			- run black and pre-commit hooks'
	@echo 'clean			- destroy all build artifacts'
	@echo 'test			- run Python unit tests'
	@echo 'build			- build the project'
	@echo 'force-release		- force a new release to be created in GitHub'
	@echo 'publish-test		- test deployment to PyPi'
	@echo 'publish-prod		- production deployment to PyPi'
