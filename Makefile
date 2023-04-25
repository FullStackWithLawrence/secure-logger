# -------------------------------------------------------------------------
# build a package for PyPi
# -------------------------------------------------------------------------
.PHONY: build requirements deps-update deps-init

requirements:
	pre-commit autoupdate
	python -m pip install --upgrade pip wheel
	pip-compile requirements/local.in
	pip install -r requirements/local.txt

deps-init:
	rm -rf .tox
	python -m pip install --upgrade pip wheel
	python -m pip install --upgrade -r requirements/local.txt -e .
	python -m pip check

deps-update:
	python -m pip install --upgrade pip-tools pip wheel
	python -m piptools compile --extra dev --upgrade --resolver backtracking -o ./requirements/local.txt pyproject.toml


report:
	cloc $(git ls-files)


build:
	python3 -m pip install --upgrade setuptools wheel twine
	python -m pip install --upgrade build

	if [ -d "./build" ]; then sudo rm -r build; fi
	if [ -d "./dist" ]; then sudo rm -r dist; fi
	if [ -d "./secure_logger.egg-info" ]; then sudo rm -r secure_logger.egg-info; fi

	python3 -m build --sdist ./
	python3 -m build --wheel ./

	python3 -m pip install --upgrade twine
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
