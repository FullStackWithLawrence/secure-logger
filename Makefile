PYTHON = python3
PIP = $(PYTHON) -m pip
.PHONY: pre-commit requirements init clean report build release-test release-prod

pre-commit:
	pre-commit install
	pre-commit run --all-files

requirements:
	pre-commit autoupdate
	$(PIP)  install --upgrade pip wheel
	python -m piptools compile --extra local --upgrade --resolver backtracking -o ./requirements/local.txt pyproject.toml
	$(PIP)  -r requirements/local.txt

init:
	python3.11 -m venv venv && \
	. venv/bin/activate && \
	rm -rf .tox && \
	$(PIP) install  --upgrade pip wheel && \
	$(PIP) install  --upgrade -r requirements/local.txt -e . && \
	python -m pip check && \
	npm install

clean:
	rm -rf build dist secure_logger.egg-info

report:
	cloc . --exclude-ext=svg,json,zip --vcs=git


build:
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
	make build
	twine upload --verbose --skip-existing --repository testpypi dist/*

# -------------------------------------------------------------------------
# upload to PyPi
# https://pypi.org/project/secure-logger/
# -------------------------------------------------------------------------
release-prod:
	make build
	twine upload --verbose --skip-existing dist/*
