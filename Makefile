PYTHON = python3
PIP = $(PYTHON) -m pip
.PHONY: pre-commit requirements init clean report build release-test release-prod

pre-commit:
	pre-commit install
	pre-commit run --all-files

requirements:
	rm -rf venv .tox .pytest_cache node_modules __pycache__ .pytest_cache
	$(PIP)  install --upgrade pip wheel
	$(PIP)  install -r requirements/local.txt && \
	npm install && \
	pre-commit install && \
	pre-commit autoupdate

init:
	python3.11 -m venv venv && \
	. venv/bin/activate && \
	make requirements


clean:
	rm -rf build dist secure_logger.egg-info

report:
	cloc . --exclude-ext=svg,json,zip --vcs=git


build:
	npx semantic-release --doctor --dry-run

	$(PIP) install  --upgrade setuptools wheel twine
	$(PIP) install  --upgrade build

	make clean

	$(PYTHON) -m build --sdist ./
	$(PYTHON) -m build --wheel ./

	$(PYTHON) -m pip install --upgrade twine
	twine check dist/*


# -------------------------------------------------------------------------
# upload to PyPi Test
# https://test.pypi.org/project/secure-logger/
# -------------------------------------------------------------------------
release-test:
	git rev-parse --abbrev-ref HEAD | grep '^main$' || (echo 'Not on main branch, aborting' && exit 1)
	make build
	twine upload --verbose --skip-existing --repository testpypi dist/*

# -------------------------------------------------------------------------
# upload to PyPi
# https://pypi.org/project/secure-logger/
# -------------------------------------------------------------------------
release-prod:
	git rev-parse --abbrev-ref HEAD | grep '^main$' || (echo 'Not on main branch, aborting' && exit 1)
	make build
	twine upload --verbose --skip-existing dist/*
